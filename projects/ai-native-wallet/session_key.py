"""Session Key — AI Agent 临时受限权限管理

Session Key 是连接 AI Agent 意图和链上执行的桥梁。
Agent 不用每次要签名，但必须在用户预设的边界内行动。

一个合格的 Session Key 至少限制 5 个维度：
  - 有效时间（valid_until）
  - 额度上限（max_per_tx_usdc, max_per_day_usdc）
  - 目标合约白名单（allowed_contracts）
  - 允许的函数签名（allowed_functions）
  - 适用链（chain_id）

Ref: Agent Wallet Handbook → Session Key 节点
     Wallet / Permission Handbook → Session Key Flow 节点
"""

from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Optional


@dataclass
class SessionKey:
    """AI Agent 使用的临时受限权限

    不应等同于"临时私钥" — 必须搭配 5 维约束使用。
    """

    key_id: str  # 唯一标识
    private_key: str  # 临时私钥（不导出给用户看）
    address: str  # 对应的 EOA 地址
    valid_from: int  # Unix timestamp
    valid_until: int  # Unix timestamp
    max_per_tx_usdc: float  # 单笔限额
    max_per_day_usdc: float  # 日限额
    allowed_contracts: list[str]  # 白名单合约地址
    allowed_functions: list[str]  # 白名单函数签名
    chain_id: int  # 适用链 ID
    status: str = "active"  # active | revoked | expired

    @classmethod
    def create(
        cls,
        valid_hours: int = 6,
        max_per_tx_usdc: float = 100.0,
        max_per_day_usdc: float = 500.0,
        allowed_contracts: Optional[list[str]] = None,
        allowed_functions: Optional[list[str]] = None,
        chain_id: int = 11155111,  # Sepolia testnet
    ) -> "SessionKey":
        """创建新的 Session Key"""
        import uuid
        from eth_account import Account

        acct = Account.create()
        now = int(datetime.now(timezone.utc).timestamp())
        return cls(
            key_id=str(uuid.uuid4())[:8],
            private_key=acct.key.hex(),
            address=acct.address,
            valid_from=now,
            valid_until=now + valid_hours * 3600,
            max_per_tx_usdc=max_per_tx_usdc,
            max_per_day_usdc=max_per_day_usdc,
            allowed_contracts=allowed_contracts or [],
            allowed_functions=allowed_functions or [],
            chain_id=chain_id,
        )

    def is_valid(self) -> tuple[bool, str]:
        """检查 Session Key 是否当前有效

        Returns:
            (is_valid, reason) — reason 在有效时为空字符串
        """
        now = int(datetime.now(timezone.utc).timestamp())
        if self.status == "revoked":
            return False, "revoked"
        if self.status == "expired" or now > self.valid_until:
            return False, "expired"
        if now < self.valid_from:
            return False, "not yet active"
        return True, ""

    def revoke(self):
        """撤销 Session Key"""
        self.status = "revoked"

    def to_dict(self) -> dict:
        """序列化为字典（不导出 private_key）"""
        return {
            "key_id": self.key_id,
            "address": self.address,
            "valid_from": self.valid_from,
            "valid_until": self.valid_until,
            "max_per_tx_usdc": self.max_per_tx_usdc,
            "max_per_day_usdc": self.max_per_day_usdc,
            "allowed_contracts": self.allowed_contracts,
            "allowed_functions": self.allowed_functions,
            "chain_id": self.chain_id,
            "status": self.status,
        }


class SessionKeyManager:
    """管理 Agent 的多把 Session Key

    功能：
    - 创建、查询、撤销 Session Key
    - 自动检测过期
    - 映射为 PermissionPolicy 可用的约束字段
    """

    def __init__(self):
        self.keys: dict[str, SessionKey] = {}

    def create(self, **kwargs) -> SessionKey:
        """创建新 Session Key 并注册到管理器"""
        sk = SessionKey.create(**kwargs)
        self.keys[sk.key_id] = sk
        return sk

    def get(self, key_id: str) -> Optional[SessionKey]:
        """按 ID 查询 Session Key"""
        return self.keys.get(key_id)

    def get_active(self) -> list[SessionKey]:
        """获取所有当前有效的 Session Key"""
        return [sk for sk in self.keys.values() if sk.is_valid()[0]]

    def revoke(self, key_id: str) -> bool:
        """撤销指定 Session Key"""
        sk = self.keys.get(key_id)
        if sk:
            sk.revoke()
            return True
        return False

    def revoke_all(self):
        """撤销所有 Session Key"""
        for sk in self.keys.values():
            sk.revoke()

    def cleanup_expired(self) -> int:
        """清理过期 Session Key，返回清理数量"""
        count = 0
        for key_id, sk in list(self.keys.items()):
            valid, reason = sk.is_valid()
            if not valid and reason == "expired":
                sk.status = "expired"
                count += 1
        return count

    def to_policy(self, sk: SessionKey) -> dict:
        """将 SessionKey 约束映射为 PermissionPolicy 可用的字段

        PermissionPolicy 期望的字段:
        - asset_whitelist, max_per_tx, max_per_day,
        - allowed_contracts, allowed_functions, valid_until
        """
        return {
            "asset_whitelist": ["USDC"],
            "max_per_tx": sk.max_per_tx_usdc,
            "max_per_day": sk.max_per_day_usdc,
            "allowed_contracts": sk.allowed_contracts,
            "allowed_functions": sk.allowed_functions,
            "valid_until": sk.valid_until,
        }


# === Quick Smoke Test ===
if __name__ == "__main__":
    print("=" * 50)
    print("SessionKey Module — Smoke Test")
    print("=" * 50)

    # Test 1: Create SessionKey
    sk = SessionKey.create(valid_hours=6, max_per_tx_usdc=100, max_per_day_usdc=500)
    print(f"\n✅ SessionKey created: {sk.key_id}")
    print(f"   Address: {sk.address}")
    print(f"   Valid until: {datetime.fromtimestamp(sk.valid_until, tz=timezone.utc)}")
    print(f"   Valid: {sk.is_valid()}")

    # Test 2: SessionKeyManager
    mgr = SessionKeyManager()
    sk1 = mgr.create(valid_hours=1, max_per_tx_usdc=50)
    sk2 = mgr.create(valid_hours=24, max_per_tx_usdc=200)
    print(f"\n✅ Manager: {len(mgr.keys)} keys, {len(mgr.get_active())} active")

    # Test 3: Revoke
    mgr.revoke(sk1.key_id)
    print(f"   After revoke sk1: {sk1.is_valid()}")
    print(f"   Active keys: {len(mgr.get_active())}")

    # Test 4: Policy mapping
    policy = mgr.to_policy(sk2)
    print(f"\n✅ Policy mapping: max_per_tx={policy['max_per_tx']}, "
          f"contracts={len(policy['allowed_contracts'])}")

    print("\n🎉 All smoke tests passed!")
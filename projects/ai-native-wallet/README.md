# AI-native Wallet

> 🏗️ AI × Web3 School Hackathon Project · Cohort 0
> 
> **方向**: 用户用自然语言描述理财目标 → AI 生成交易意图 → Permission System 校验边界 → Smart Account 执行
>
> **核心洞察**: Agent 不应该持有私钥，它只应该拥有一组可限制、可审计、可撤销的能力。

## 项目 Pitch

An AI-native wallet that lets users delegate spending permissions to AI agents with programmable limits. The AI handles transaction intent (what to buy, when to swap), while on-chain smart accounts enforce hard constraints (max spend, allowed protocols, time windows). This makes DeFi accessible to non-technical users — they describe goals in natural language, and the wallet executes within guardrails.

## 核心流程

```
User (Natural Language Intent)
        ↓
AI Agent (Parse intent → Generate transaction plan)
        ↓
Permission Policy System (Validate: asset, amount, contract, time)
        ↓
Smart Account (Execute within guardrails via Session Key)
        ↓
Blockchain (Settlement + logs + audit trail)
```

## 技术栈

- **Backend**: Python (web3.py, eth-account)
- **Frontend**: TBD (React/Next.js or pure CLI demo)
- **Smart Account**: ERC-4337 (Safe{Wallet} or Biconomy)
- **RPC**: Public endpoints (llamarpc, infura)

## 两周 Milestone

| Week | Goal |
|------|------|
| Week 1 | Permission Policy 数据模型 + Smart Account 部署 + Session Key 创建 |
| Week 2 | AI intent parser + 端到端 demo: 自然语言 → 链上交易 |
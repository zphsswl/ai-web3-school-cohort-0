#!/usr/bin/env python3
"""Hello Chain — First on-chain query for AI-native Wallet project.

Verifies RPC connectivity and fetches basic chain state.
Run: python hello_chain.py
"""

from web3 import Web3

# Public RPC endpoint
RPC_URL = "https://eth.llamarpc.com"

def main():
    w3 = Web3(Web3.HTTPProvider(RPC_URL))

    # 1. Connection check
    if not w3.is_connected():
        print("❌ Failed to connect to Ethereum RPC")
        return

    print(f"✅ Connected to Ethereum")
    print(f"   Chain ID: {w3.eth.chain_id}")

    # 2. Latest block
    block = w3.eth.get_block('latest')
    print(f"\n📦 Latest Block: #{block['number']}")
    print(f"   Timestamp: {block['timestamp']}")
    print(f"   Transactions: {len(block['transactions'])}")

    # 3. Gas price
    gas_price = w3.eth.gas_price
    print(f"\n⛽ Gas Price: {w3.from_wei(gas_price, 'gwei'):.2f} gwei")

    # 4. Sample balance (Ethereum Foundation)
    ef_address = "0xde0B295669a9FD93d5F28D9Ec85E40f4cb697BAe"
    balance = w3.eth.get_balance(ef_address)
    print(f"\n💰 EF Balance: {w3.from_wei(balance, 'ether'):.2f} ETH")

    # 5. ENS lookup (vitalik.eth)
    try:
        vitalik = w3.ens.address('vitalik.eth')
        print(f"\n🔗 vitalik.eth → {vitalik}")
    except Exception:
        print(f"\n🔗 ENS lookup skipped (may not be supported on this RPC)")

    print(f"\n🎉 Ready to build! Permission Policy scaffold next.")

if __name__ == "__main__":
    main()
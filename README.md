     1|# AI × Web3 School — Personal Learning Journal
     2|
     3|> Cohort 0 · Personal learning journal and proof-of-work for [AI × Web3 School](https://aiweb3.school).
     4|>
     5|> 🐦 Twitter: follow [@LXDAO_Official](https://x.com/LXDAO_Official) [@ETHPanda_Org](https://x.com/ETHPanda_Org) [@aiweb3school](https://x.com/aiweb3school) [@Zai_org](https://x.com/Zai_org) [@web3careerbuild](https://x.com/web3careerbuild) · [#AIxWeb3School](https://x.com/hashtag/AIxWeb3School)
     6|
     7|---
     8|
     9|## 🗞️ Week 1 学习总结 · Phase 1: Web3 Foundations ✅
    10|
    11|Phase 1 收工，9 天 9 章，从 Network 一路啃到 Security。本人 AI 背景还行但 Web3 一直停在「用过钱包、知道合约是什么」的水平，这周算是第一次系统地把链上基础设施过了一遍。
    12|
    13|### 1. 重新理解的 AI 概念：Agent ≠ Workflow
    14|
    15|之前觉得 Agent 就是给 LLM 接几个工具让它自己跑。这周写 daily note、搭 Learning Agent 的过程中意识到一个关键区别：**Workflow 是固定管道，Agent 是自主决策循环**。Workflow 适合步骤明确的重复任务（比如每天早上抓 Handbook 生成笔记），Agent 适合目标模糊、需要根据中间结果动态调整的场景。一个好的 Agent = LLM + Tools + Memory + Planning + Guardrails，五个要素缺一不可，尤其是 Guardrails——没有安全边界的 Agent 在 Web3 场景下就是定时炸弹。
    16|
    17|### 2. 重新理解的 Web3 概念：签名 ≠ 登录
    18|
    19|以前觉得「用钱包签名」就是 Web3 版的「输入密码登录」。学完 Cryptography + Wallet 两章才搞清楚：**签名是授权一笔具体操作的证据，不是确认身份**。connect（连接钱包）、sign（签名消息）、send（发送交易）是三个完全不同的风险等级——connect 只是读取地址，sign message 可以证明「这个地址同意这段话」，send transaction 直接动链上状态。很多钓鱼网站就是利用用户「签名=登录」的误解，骗你签一笔 approve 或 transfer 的交易。
    20|
    21|另外私钥 = 控制权这个认知太重要了。链上没有「找回密码」，没有「管理员重置」，丢了私钥就是丢了身份。
    22|
    23|### 3. AI × Web3 交叉问题：Agent 什么时候可以动钱？
    24|
    25|这周最大的思考是：**Agent 可以发起支付，但必须分层设限**。我的 mental model：
    26|
    27|- **只读层（安全）**：查余额、读交易历史、监控仓位 → Agent 随便跑
    28|- **建议层（需要验证）**：推荐策略、生成交易草稿 → Agent 输出，人类复核
    29|- **受限执行层（需要 policy）**：小额 swap、定时定投 → Agent 可以自动执行，但有金额上限、协议白名单、slippage 约束
    30|- **禁止层（必须人类确认）**：大额转账、合约部署、权限变更、approve 授权 → 绝不能让 Agent 自行决定
    31|
    32|另外 Simulation 是 Agent 的安全阀——每笔 AI 生成的交易执行前应该用 Tenderly 模拟一遍，确认调哪个合约、转出什么、gas 多少、会不会 revert。
    33|
    34|### 4. Proof-of-Work
    35|
    36|- 📂 **GitHub Repo**: [zphsswl/ai-web3-school-cohort-0](https://github.com/zphsswl/ai-web3-school-cohort-0)
    37|  - 9 篇 daily notes（每天都有打卡草稿 + 三条学习路径）
    38|  - 完整 learning-plan.md + profile.md
    39|  - 用 Hermes Agent 搭了自动化学习助手（每天 8:00 晨间推送 + 21:00 晚间回顾，定时 cron）
    40|- 📝 **输出物**：
    41|  - 10 个 AI 核心概念速通笔记（LLM / Prompt / Context Window / Workflow / Agent / Tool Use / AI Coding / Guardrails / Tracing / Human-in-the-loop）
    42|  - DeFi Agent 安全策略设计（5 个必检查项 + AI 操作分级）
    43|  - Phase 1 安全全景图（设计→审计→模拟→监控→应急，全链路）
    44|  - 交易安全检查表（对公开交易做 from/to/method/value/token transfers 五维分析）
    45|- 🤖 **Learning Agent**: 自动化每日学习内容生成 + Git 提交，算是 AI × Web3 的第一手实践
    46|
    47|### 5. 还没解决的问题 & Week 2 方向
    48|
    49|- **Tenderly Simulation 实操**：理论理解了，还没真正跑过一笔模拟交易，这周必须动手
    50|- **Smart Account (AA) 和 Agent Wallet 的区别**：看了 Account Abstraction 章节但感觉理解还浅，Phase 2 的 Agent Wallet 章节能补上
    51|- **Prompt Injection 在 Web3 场景下的攻击面**：如果一个 Agent 能从链上读数据生成交易，恶意合约的 event 日志能注入 prompt 吗？
    52|
    53|Week 2 进入 Phase 2（AI × Web3 Bridge），最期待的是 **Agent Wallet** 和 **Machine Payment** 两章——终于从「理解基础设施」进入「AI 怎么实际操作链」了。
    54|
    55|---
    56|
    57|## 📚 Quick Links
    58|
    59|- [Handbook (中文)](https://aiweb3.school/zh/handbook/)
    60|- [WCB Bootcamp 课程页](https://web3career.build/zh/programs/AI-Web3-School)
    61|- [WCB Learning 页](https://web3career.build/zh/programs/AI-Web3-School#tab=learning)
    62|- [GitHub Repo](https://github.com/zphsswl/ai-web3-school-cohort-0)
    63|
    64|## 🗂️ Repo Structure
    65|
    66|| Directory | Purpose |
    67||-----------|---------|
    68|| `daily/` | Daily learning notes & check-in drafts |
    69|| `tasks/` | Task breakdowns and completions |
    70|| `experiments/` | Code experiments, prototypes, PoCs |
    71|| `handbook-feedback/` | Feedback, errata, and suggestions for the Handbook |
    72|| `hackathon/` | Hackathon ideas, notes, and project materials |
    73|| `submissions/` | Bootcamp assignment submissions |
    74|| `templates/` | Note templates for daily & task |
    75|
    76|## 👤 Profile
    77|
    78|See [profile.md](profile.md) — AI 🔵 · Web3 🟡 · Scripting 🟡
    79|
    80|## 📖 Learning Plan
    81|
    82|See [learning-plan.md](learning-plan.md) — Phase 1 ✅ → Phase 2 进行中
    83|
    84|## ⚠️ Privacy Notice
    85|
    86|This repository is **public**. DO NOT commit:
    87|- API keys, secrets, or tokens
    88|- Private keys or seed phrases
    89|- Personal contact information
    90|- Internal meeting links
    91|- Other people's personal data
    92|
    93|---
    94|
    95|> Built with AI × Web3 School Learning Agent · 2026
    96|
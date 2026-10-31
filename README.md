# 语义通信 × 多智能体协同感知：新人研究生调研笔记

> 面向刚入门的研究生，梳理「语义通信 / 任务导向通信」视角下的多智能体协同感知（车车 V2V、车路 V2I/V2X、无人机群）。
> 资料截至 **2026-10-31**。各章由 GPT-6 Astra 子 agent 联网调研撰写，主 agent 负责汇总和抽查；未能核实的条目在正文中标注为「待核实」。

## 目录

| 章节 | 内容 | 适合谁 |
|---|---|---|
| [01 协同感知基础与研究脉络](<chapters/01-基础与脉络.md>) | 问题定义、早/中/晚期融合、代表方法（Cooper → HEAL → CodeFilling/CPPC/CauseCollab/RSTA）、数据集、评价指标、关键挑战、时间线 | 所有人，从这里开始 |
| [02 语义通信与任务导向通信视角](<chapters/02-语义通信与协同感知.md>) | Shannon–Weaver 三层问题、DeepJSCC、信息瓶颈、语义率失真；Who2com/When2com/Where2comm/What2comm/CodeFilling/PragComm；SComCP、InfoCom、语义 ISAC、LLM 语言级/潜在协同；通信与 CV 社区的视角对比 | 想做“通信 × 感知”交叉方向的同学 |
| [03 入门路线、工具链与开放问题](<chapters/03-入门路线与开放问题.md>) | 前置知识与教材、必读论文、开源框架与仿真平台、8–12 周学习计划、团队与综述、开放问题与选题建议 | 准备上手复现、选题的同学 |

## 推荐的最短阅读路径

1. **建立直觉**：OPV2V（AttFuse）→ F-Cooper → V2VNet
2. **学会“传什么”**：Where2comm → CodeFilling → PragComm / CPPC
3. **面对真实约束**：CoAlign（位姿误差）→ HEAL（异构）→ SComCP / InfoCom（信道与信息瓶颈）
4. **按兴趣扩展**：DeepJSCC、语义率失真（理论）；语义 ISAC（通感一体化）；LangCoop、LACO、AirCopBench（大模型）

## 第一个动手实验建议

在 OpenCOOD 或 HEAL 框架上复现 OPV2V 的单车 / 晚期 / 中期融合基线，再接入 Where2comm 式的空间稀疏选择，画出**检测 AP–实际传输字节数**曲线。注意把位置索引、量化位宽和元数据都算进字节数。

## 仓库结构

```
.
├── README.md                 # 本文件：总览与导航
├── chapters/                 # 各章调研正文（Markdown）
└── scripts/
    └── extract_chapters.py   # 从子 agent 工作流输出中提取章节的辅助脚本
```

## 使用说明与免责声明

- 论文和代码链接由子 agent 联网核实，主 agent 抽查了部分 2025–2026 年新论文的 arXiv 页面。引用前请再到原始出处核对一遍。
- 仓库链接能访问不代表代码能直接复现；维护状态以对应日期的 GitHub 元数据为准。
- 欢迎在阅读时直接修改补充，用 git 记录自己的阅读笔记和复现记录。

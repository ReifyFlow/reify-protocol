# ReifyFlow Protocol

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Status: MVP](https://img.shields.io/badge/Status-MVP_Dev-orange.svg)]()

**ReifyFlow 生态系统的核心数据契约 (Data Contracts) 与交互标准。**

本项目存放所有 AI Agent、工具链与嵌入式硬件之间通信的 **JSON Schema** 定义及标准 C 头文件。

## 🛠️ Protocol Definition (协议简述)
---

# 🌌 ReifyFlow Protocol: A Universal Framework for Neuro-Symbolic Manifestation
**(ReifyFlow 协议：神经符号显化的通用框架)**

**Version:** 1.0 (Concept Draft)
**Classification:** System Architecture / AI Grounding

---

## 1. 核心论题 (Core Thesis)

当前人工智能（AI）的发展遭遇了**“语义与现实的阻抗不匹配” (Semantic-Reality Impedance Mismatch)**。
* **AI (L1/L2):** 存在于概率性的、无限的、非竞争性的**文本共识**中。
* **Reality (L3/L4):** 存在于确定性的、有限的、排他性的**物理约束**中。

**ReifyFlow** 旨在定义一种通用的**“显化协议” (Manifestation Protocol)**。它不直接生成代码，而是构建一个**“中间态的坍缩场”**，通过**意图与约束的协商 (Negotiation)**，将无限的智能安全、有效地转化为有限的物理现实。

**核心公理：意图即现实 (Intent is Reality)。**
现实并非独立存在，它是意图在通过物理约束层层坍缩后留下的轨迹。

---

## 2. 本体论架构 (Ontological Architecture)

系统基于**分形递归 (Fractal Recursion)** 的四层模型。任何实体（无论是人类、AI Agent、芯片还是工厂）均被视为该模型的实例。

### Layer 1: 意识层 (The Layer of Will)
* **定义：** **意图分子 (Intent Molecules)** 的集合。
* **属性：** **非竞争性 (Non-rivalrous)**。
    * 意图是并发的、混沌的、只有目的（Why）而无过程（How）。
    * *特征：* 无时间性（Timeless）。
* **数据载体：** 自然语言 Prompt 或 Agent 的元目标 (Meta-Goal)。

### Layer 2: 理想层 (The Layer of Logic)
* **定义：** **逻辑拓扑 (Logical Topology)**。
* **属性：** **因果有序 (Causal)**。
    * 意图在此层被解析为完美的数学关系或数据流图。
    * *特征：* 序列性（Sequence），时间表现为相位（Phase）。
* **数据载体：** 虚拟节点图 (Virtual Graph)。

### Layer 3: 物理层 (The Layer of Vessel)
* **定义：** **资源容器 (Resource Container)**。
* **属性：** **排他性 (Exclusival)**。
    * 这是现实的模具。它定义了带宽、算力、能量、空间等刚性边界。
    * *特征：* 预算性（Budget），时间表现为代价/资源。
* **数据载体：** 约束描述文件 (Constraint Schema / SVD)。

### Layer 4: 反馈层 (The Layer of Sensation)
* **定义：** **熵增过程 (Entropic Process)**。
* **属性：** **不可逆性 (Irreversible)**。
    * 这是意图显化为电流、运动或热量的过程。它是唯一的真理来源。
    * *特征：* 流动性（Flow），包含误差与痛觉（Error/Pain）。
* **数据载体：** 遥测数据 (Telemetry) 与 物理现象。

---

## 3. 运行机制：耦合与坍缩 (Mechanisms)

传统的控制论是“指令式”的，ReifyFlow 是**“生成式与约束式”的辩证统一**。

### 3.1 缘起性耦合 (Dependent Coupling)
意图不是孤立存在的点，而是依赖物理环境存在的网。
* **启示 (Affordance):** 物理层 (L3) 主动向上暴露能力（如：“我有硬件加速器”）。
* **试探 (Probing):** 意图层 (L1) 向下发出模糊倾向（如：“我需要高效计算”）。
* **协商 (Negotiation):** 两者在接触面发生**波函数坍缩**，确定唯一的实现路径。

### 3.2 结构即法律 (Structure is Law)
系统不依赖事后的代码检查（Linting），而是依赖**前置的类型定义**。
* **构造即否定：** 描述文件中未定义的可能性，在物理上即被视为不存在。
* **合法性校验：** 通过**子图同构算法 (Subgraph Isomorphism)**，验证意图小网能否嵌入物理大网。

### 3.3 双回环验证 (Dual-Loop Verification)
* **内环 (SIL):** 在 L2 层面验证逻辑的自洽性（无时间维度的正确性）。
* **外环 (HIL):** 在 L4 层面验证物理的真实性（熵增维度的正确性）。**物理反馈是修正意图的唯一依据。**

---

## 4. 协议定义：ReifyGraph (The Protocol)

核心资产是一套通用的世界描述语言规范：**`world_graph.json`**。

### 4.1 节点类型 (Node Types)
* **Intent Node:** 承载目的（Origin）。
* **Virtual Node:** 承载算法（Transform）。
* **Physical Node:** 承载资源（Constraint）。

### 4.2 互含因果 (Reciprocal Causality)
协议支持**分形引用 (Fractal Import)**。
* 一个系统的 L4 (输出/现实) 可以直接作为另一个系统的 L3 (输入/约束)。
* *例:* 电网系统的 L4 (供电稳定性) 成为 嵌入式系统的 L3 (电源约束)。

---

## 5. 交互范式 (Interaction Paradigm)

**Chat-to-Graph (对话生成图谱)**

1.  **Input:** 自然语言或高阶 Agent 指令。
2.  **Visualization:**
    * **虚线/光晕:** 表示正在协商中的“叠加态意图”。
    * **实线/红色:** 表示已坍缩的“现实”或物理冲突的“痛点”。
3.  **Action:** 人类（或上层仲裁者）只需处理**冲突**和**价值排序**，无需处理实现细节。

---

## 6. 执行路线图 (Execution Roadmap)

本项目旨在构建物理计算的基础设施，而非单一工具。

* **Phase I: Kernel (内核期)**
    * 目标：验证“意图-物理”的拓扑映射逻辑。
    * 产出：Protocol v0.1 定义，约束求解引擎原型。
* **Phase II: Intelligence (智能期)**
    * 目标：接入 LLM，实现“自然语言 -> 结构化意图”的转化。
    * 产出：Reify-Core (AI Agent)，具备初步的物理常识。
* **Phase III: Manifestation (显化期)**
    * 目标：接入真实硬件，打通 HIL 物理回环。
    * 产出：Reference Implementation (基于 STM32 的完整闭环演示)。

---

## 7. 结语 (Conclusion)

ReifyFlow 不是为了替代工程师，而是为了**释放意图**。
它是一座桥梁，连接了**“碳基/硅基的灵感”**与**“坚硬的物理世界”**。
通过将物理约束数字化、结构化，我们终将实现：**万物皆可编程，意图即是现实。**
---

*Created for ReifyFlow.*

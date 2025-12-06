# ReifyFlow Protocol

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Status: MVP](https://img.shields.io/badge/Status-MVP_Dev-orange.svg)]()

**ReifyFlow 生态系统的核心数据契约 (Data Contracts) 与交互标准。**

本项目存放所有 AI Agent、工具链与嵌入式硬件之间通信的 **JSON Schema** 定义及标准 C 头文件。

## 📂 Repository Structure (仓库结构)

```text
reify-protocol/
├── schemas/                  # [核心] JSON 格式标准定义
│   ├── software.schema.json      # 软件需求与架构定义
│   ├── hardware.schema.json      # 硬件资源映射定义
│   └── log_frame.schema.json     # 回环日志数据帧定义
│
├── examples/                 # [参考] 标准 JSON 样例 (用于测试/Prompt)
│   ├── demo_task.json            
│   └── stm32f103_map.json
│
├── firmware/                 # [嵌入式] C 语言标准头文件
│   └── reify_log.h               # 日志结构体定义
│
└── LICENSE                   # MIT 开源协议
```

## 🛠️ Protocol Definition (协议简述)

目前定义了三个核心交互域：

1.  **Software Spec**: 定义业务逻辑流（与芯片无关）。
2.  **Hardware Map**: 定义引脚分配与外设配置（与芯片强相关）。
3.  **Telemetry**: 定义嵌入式设备回传给 PC 的日志格式。

## 🚀 Usage (使用)

### Python (工具链开发)
直接引用 `schemas/` 目录下的 JSON 文件进行校验。

### Firmware (嵌入式开发)
将 `firmware/reify_log.h` 复制到您的 MCU 工程中以启用标准日志回传。

---
*Created for ReifyFlow.*

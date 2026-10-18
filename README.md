# 🌤️ 天气穿搭助手——WeatherOutfitAdvisor 

> **“不被风格定义，只让你在任何天气下都能穿着合适。”**

这是一个基于大语言模型（LLM）与检索增强生成（RAG）的智能穿搭决策系统。本项目旨在解决用户在日常通勤、旅行中“看天穿衣”的痛点，同时结合**国货大众品牌**定位，提供具备真实性、高性价比的穿搭建议。

## ✨ 核心特性 (Features)

* **🌦️ 实时天气感知**：接入和风天气 API，精准提取城市气温、湿度、紫外线及风力数据。
* **🎨 风格约束**：通过 Prompt Engineering 注入“低饱和度、版型修饰、微阔垂坠”等风格基调，拒绝千篇一律的模板化推荐。
* **💰 真实的品牌与价格对标**：拒绝“虚假高档”，材质与定价紧贴国内大众品牌，例如：选择优衣库、TOPTEN10、以纯、鹿岛、骆驼这五个大众品牌，单品价格透明，套装支持 9 折单品叠加折扣计算。
* **🧠 结构化 RAG 检索**：自建材质库（`material_guide.json`）与风格库（`style_guide.json`），根据气候特征动态加载约束条件。
* **⚖️ 基于 CheckEval 的质量验证**：引入二元 Checklist 评估机制，从温度逻辑、分层完整、材质具体等 6 个维度验证输出质量，做到通过率 100%。

## 🛠️ 技术栈 (Tech Stack)

* **语言**：Python 3.11
* **Agent 框架**：LangChain 1.4.4 (基于 LangGraph) + ReAct 模式
* **大语言模型**：DeepSeek V4.1 Flash (通过 OpenAI 兼容接口接入)
* **外部工具**：和风天气 API
* **前端 UI**：Gradio (规划中)
* **环境管理**：Conda

## 🚀 快速开始 (Quick Start)

1. 克隆项目并安装依赖：
   ```bash
   git clone https://github.com/jaemren0819/weather-outfit-advisor.git
   cd weather-outfit-advisor
   conda create -n weather-outfit python=3.11
   conda activate weather-outfit
   pip install -r requirements.txt

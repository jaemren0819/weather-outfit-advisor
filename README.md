# 🌤️ WeatherOutfitAdvisor (智能天气穿搭推荐引擎)

> **“不被风格定义，只让你在任何天气下都能穿着合适。”**

本项目是一个基于大语言模型（LLM）与检索增强生成（RAG）的智能穿搭推荐引擎。项目旨在解决用户在看天穿衣、多场景切换时的决策痛点，并通过结构化知识库，提供符合 **韩系 Clean Fit 风格**、适配 **真实消费预算**（对标国内大众品牌）的个性化穿搭方案。

## 📸 界面预览 (UI Preview)

<img width="1037" height="621" alt="屏幕截图 2026-10-22 225957" src="https://github.com/user-attachments/assets/296b5b3f-aa9a-42fc-bdb8-7816d8f5788b" />

## ✨ 核心特性 (Features)

* **🌦️ 实时天气感知**：接入和风天气 API，精准提取目标城市的气温、湿度、紫外线及降水概率，动态应对日夜温差。
* **🎨 韩系 Clean Fit 风格约束**：通过强 Prompt 约束与风格检索，拒绝千篇一律的推荐。主打低饱和度（莫兰迪色系）与修身版型（微阔、落肩），提升大众单品的穿搭质感。
* **💰 多档预算与国货品牌对标**：拒绝“虚假高档”。引入品牌梯队 RAG（如学生党-鹿岛/以纯，上班族-优衣库/TOPTEN10），提供单品真实价格与套装折扣计算，实现精准导购。
* **🧠 结构化 RAG 检索架构**：自建材质库（`material_guide.json`）与风格库（`style_guide.json`），Agent 根据天气和用户需求，自动调用并过滤匹配的材质与品牌。
* **⚖️ 基于规则的二元校验**：引入前沿的 LLM 评估方法论（借鉴 CheckEval 思想），通过自动化脚本校验 LLM 是否严格遵循了用户的预算约束，防止“预算幻觉”。

## 🛠️ 技术栈 (Tech Stack)

* **开发语言**：Python 3.11
* **Agent 框架**：LangChain 1.4.4 (基于 LangGraph) + ReAct 模式
* **大语言模型**：DeepSeek V4.1 Flash (通过 OpenAI 兼容接口接入)
* **外部数据**：和风天气 API
* **Web 前端**：Gradio (支持快速交互与 Markdown 渲染)
* **环境管理**：Conda

## 🚀 快速开始 (Quick Start)

### 1. 克隆项目与安装依赖
```bash
git clone https://github.com/jaemren0819/weather-outfit-advisor.git
cd weather-outfit-advisor
conda create -n weather-outfit python=3.11
conda activate weather-outfit
pip install -r requirements.txt

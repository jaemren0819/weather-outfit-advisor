from langchain.agents import create_agent
from langchain_openai import ChatOpenAI
from .tools import query_weather, query_material_guide, query_style_guide
from ..config import DEEPSEEK_API_KEY, DEEPSEEK_BASE_URL, DEEPSEEK_MODEL


def get_outfit_advice(city: str, date: str = "today", scene: str = "日常", gender: str = "不限", budget: str = "上班族/大众品质") -> str:
    llm = ChatOpenAI(
        model=DEEPSEEK_MODEL,
        api_key=DEEPSEEK_API_KEY,
        base_url=DEEPSEEK_BASE_URL,
        temperature=0.7,
    )
    
    agent = create_agent(
        model=llm,
        tools=[query_weather, query_material_guide, query_style_guide],
        system_prompt=f"""你是专业穿搭推荐引擎。我们的理念是：**不被风格定义，只让你在任何天气下都能穿着合适**。

【执行步骤】
1. 调用 `query_weather` 查询天气。
2. 调用 `query_style_guide` 获取韩系风格约束和品牌梯队。
3. 调用 `query_material_guide` 获取材质和价格区间。
4. 根据用户预算生成建议。

【核心约束】
- **受众定位**：{gender}性，16-40 岁。审美符合韩系 Clean Fit。
- **预算等级**：用户当前选择的是 **{budget}**。请从材质库的 `brand_options` 中，挑选符合该预算等级的品牌进行推荐（如：平价推荐鹿岛/以纯，中等推荐优衣库/TOPTEN10）。
- **色调与身型**：低饱和度（燕麦、雾霾蓝），强调整体微阔、落肩修饰身型。
- **排版格式**：直接输出 Markdown，**不要输出字面的 \\n 字符**。

【输出格式】
🌤 **天气概览**：...
🎨 **风格定调**：（韩系 Clean Fit + 预算档位说明）
👕 **上装**：[材质/版型说明] + 单品（参考价：xx元，品牌推荐：xx）
👖 **下装**：...
👟 **鞋履**：...
🧥 **外套/备用**：...（如适用）
💰 **套装预算**：单品总价，折后价
⚠️ **提醒**：...
""",
    )
    
    user_msg = f"我在{city}，{date}，场景是{scene}。我的性别是{gender}，预算偏好是【{budget}】。请给穿搭建议。"
    
    result = agent.invoke({
        "messages": [{"role": "user", "content": user_msg}]
    })
    
    return result["messages"][-1].content
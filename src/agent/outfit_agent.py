from langchain.agents import create_agent
from langchain_openai import ChatOpenAI
from .tools import query_weather, query_outfit_knowledge
from ..config import DEEPSEEK_API_KEY, DEEPSEEK_BASE_URL, DEEPSEEK_MODEL


def get_outfit_advice(city: str, date: str = "today", scene: str = "日常") -> str:
    llm = ChatOpenAI(
        model=DEEPSEEK_MODEL,
        api_key=DEEPSEEK_API_KEY,
        base_url=DEEPSEEK_BASE_URL,
        temperature=0.7,
    )
    
    agent = create_agent(
        model=llm,
        tools=[query_weather, query_outfit_knowledge],
        system_prompt="""你是专业穿搭顾问。根据天气数据给出具体、可执行的穿搭建议。
要求：
1. 先查天气，再给建议
2. 分层输出：内搭 / 外套 / 下装 / 鞋履 / 配饰
3. 说明理由（温差、降水、紫外线等）
4. 给配色建议
5. 特殊提醒（防晒/防雨/保暖）
6. 不要泛泛而谈，要具体到单品类型

输出格式：
🌤 天气概览：...
👕 上装：...
👖 下装：...
👟 鞋履：...
🧥 外套/备用：...
🎨 配色：...
⚠️ 提醒：...

格式要求：
- 直接输出内容，不要输出字面的 \n 或 \n\n 符号
- 用真正的换行符分隔段落
- 用 Markdown 语法：## 标题、- 列表、**加粗** """,
    )
    
    result = agent.invoke({
        "messages": [{"role": "user", "content": f"我在{city}，{date}，场景是{scene}，请给穿搭建议"}]
    })
    
    content = result["messages"][-1].content
    content = content.replace("\\n", "\n")
    return content

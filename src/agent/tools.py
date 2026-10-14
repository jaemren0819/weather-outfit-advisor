from langchain.tools import tool
from ..weather.client import WeatherClient

weather_client = WeatherClient()


@tool
def query_weather(city: str, date: str = "today") -> str:
    """查询指定城市和日期的天气。date 支持 today 或 tomorrow"""
    info = weather_client.get_weather(city, date)
    return info.to_prompt_text()


@tool
def query_outfit_knowledge(query: str) -> str:
    """检索穿搭知识库，query 如 15度通勤、雨天约会"""
    return "知识库暂未加载，请根据常识给出建议。"
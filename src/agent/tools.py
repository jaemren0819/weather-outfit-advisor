import json
import os
from langchain.tools import tool
from ..weather.client import WeatherClient

weather_client = WeatherClient()

@tool
def query_weather(city: str, date: str = "today") -> str:
    """查询指定城市和日期的天气。date 支持 today 或 tomorrow"""
    info = weather_client.get_weather(city, date)
    return info.to_prompt_text()

@tool
def query_material_guide(climate_type: str, temp_range: str) -> str:
    """
    根据气候类型和温度区间查询材质与价格指南。
    参数 climate_type: 例如 '南方湿热', '北方干冷', '昼夜温差大'
    参数 temp_range: 例如 '20-30', '0-10'
    """
    try:
        with open("data/material_guide.json", "r", encoding="utf-8") as f:
            guides = json.load(f)
        
        # 简易匹配
        for guide in guides:
            if climate_type in guide.get("climate", ""):
                return json.dumps(guide, ensure_ascii=False, indent=2)
        
        return "未找到精确匹配的材质指南，请根据常识给出符合大众品牌定位的建议。"
    except Exception as e:
        return f"读取材质库失败: {e}"

@tool
def query_style_guide() -> str:
    """获取应用的核心穿搭风格约束（包括受众、品牌对标和风格铁律）"""
    try:
        with open("data/style_guide.json", "r", encoding="utf-8") as f:
            style = json.load(f)
        return json.dumps(style, ensure_ascii=False, indent=2)
    except Exception as e:
        return f"读取风格库失败: {e}"
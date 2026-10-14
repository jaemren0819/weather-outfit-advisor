import os
from dotenv import load_dotenv

load_dotenv()

# DeepSeek
DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY")
DEEPSEEK_BASE_URL = "https://api.deepseek.com/v1"
DEEPSEEK_MODEL = "deepseek-flash"

# 和风天气
QWEATHER_KEY = os.getenv("QWEATHER_KEY")
QWEATHER_HOST = os.getenv("QWEATHER_HOST", "https://devapi.qweather.com")

# Embedding
EMBEDDING_MODEL = "BAAI/bge-small-zh-v1.5"

# 缓存
WEATHER_CACHE_TTL = 1800
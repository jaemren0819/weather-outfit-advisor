import requests
from .models import WeatherInfo
from ..config import QWEATHER_KEY, QWEATHER_HOST


class WeatherClient:
    def _get_location_id(self, city: str) -> str:
        resp = requests.get(
            f"{QWEATHER_HOST}/geo/v2/city/lookup",
            params={"location": city, "key": QWEATHER_KEY},
        )
        data = resp.json()
        if data.get("code") == "200" and data.get("location"):
            return data["location"][0]["id"]
        raise ValueError(f"未找到城市：{city}")

    def get_weather(self, city: str, date: str = "today") -> WeatherInfo:
        location_id = self._get_location_id(city)
        resp = requests.get(
            f"{QWEATHER_HOST}/v7/weather/3d",
            params={"location": location_id, "key": QWEATHER_KEY},
        )
        data = resp.json()
        if data.get("code") != "200":
            raise ValueError(f"天气查询失败：{data}")

        daily = data["daily"]
        idx = 0 if date == "today" else 1 if date == "tomorrow" else 0
        day = daily[idx]

        return WeatherInfo(
            city=city,
            date=day["fxDate"],
            temp_min=float(day["tempMin"]),
            temp_max=float(day["tempMax"]),
            condition=day["textDay"],
            wind=day["windDirDay"] + day["windScaleDay"] + "级",
            humidity=int(day["humidity"]),
            uv=day.get("uvIndex", "未知"),
            precipitation=float(day.get("precip", 0)),
        )
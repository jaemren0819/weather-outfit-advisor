from dataclasses import dataclass


@dataclass
class WeatherInfo:
    city: str
    date: str
    temp_min: float
    temp_max: float
    condition: str
    wind: str
    humidity: int
    uv: str
    precipitation: float

    def to_prompt_text(self) -> str:
        return f"""城市：{self.city}
日期：{self.date}
气温：{self.temp_min}~{self.temp_max}℃
天气：{self.condition}
风力：{self.wind}
湿度：{self.humidity}%
紫外线：{self.uv}
降水概率：{self.precipitation}%"""
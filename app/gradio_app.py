import gradio as gr
import os
import sys

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if project_root not in sys.path:
    sys.path.insert(0, project_root)
os.chdir(project_root)

from src.agent.outfit_agent import get_outfit_advice

# 定义 Gradio 的交互逻辑
def advise_ui(city, date, scene, gender, budget):
    if not city:
        return "请输入城市名称"
    
    # 简单的中文日期映射
    date_map = {"今天": "today", "明天": "tomorrow"}
    date_en = date_map.get(date, "today")
    
    try:
        # 调用你的 Agent
        result = get_outfit_advice(city, date_en, scene, gender, budget)
        return result
    except Exception as e:
        return f"error：{str(e)}\n请检查终端输出或 API 余额。"


with gr.Blocks(title="WeatherOutfitAdvisor", theme=gr.themes.Soft(primary_hue="blue", neutral_hue="slate")) as demo:
    gr.Markdown(
        """
        # 🌤️ WeatherOutfitAdvisor
        > **“不被风格定义，只让你在任何天气下都能穿着合适。”**
        
        基于大语言模型的智能穿搭推荐引擎。为你提供符合 **韩系 Clean Fit** 风格、适配你真实预算的智能推荐方案。
        """
    )
    
    with gr.Row():
        with gr.Column(scale=1):
            city_input = gr.Textbox(label="城市", placeholder="例如：广州、北京", value="广州")
            date_input = gr.Radio(choices=["今天", "明天"], label="日期", value="明天")
            scene_input = gr.Dropdown(
                choices=["日常", "通勤", "约会", "运动", "旅游", "海边"], 
                label="场景", value="通勤"
            )
            gender_input = gr.Radio(choices=["不限", "男", "女"], label="性别", value="不限")
            budget_input = gr.Dropdown(
                choices=["学生党/极致性价比", "上班族/大众品质", "轻户外/功能性"], 
                label="预算偏好", value="上班族/大众品质"
            )
            
            submit_btn = gr.Button("✨ 生成穿搭建议", variant="primary")
            
        with gr.Column(scale=2):
            output_markdown = gr.Markdown(label="穿搭建议", value="*等待生成...*")
    
    # 绑定按钮点击事件
    submit_btn.click(
        fn=advise_ui,
        inputs=[city_input, date_input, scene_input, gender_input, budget_input],
        outputs=output_markdown
    )

if __name__ == "__main__":
    demo.launch(server_name="127.0.0.1", server_port=7860)
import os
import google.generativeai as genai
from dotenv import load_dotenv

# ✅ 加载 .env 环境变量
load_dotenv()

# ✅ 配置 Gemini API Key
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# ✅ 使用明确的模型名（适配 v1 接口）
model = genai.GenerativeModel("gemini-1.0-pro")

def get_health_advice(symptom: str) -> str:
    print("🚀 正在调用 Gemini 模型，症状内容:", symptom)

    prompt = f"""
你是一位中文家庭医生，请根据以下症状提供简洁、实用的健康建议：

症状：{symptom}

要求：
- 用中文回答
- 包括可能原因、建议措施、是否建议就医
- 建议用换行分段描述
"""

    try:
        response = model.generate_content(prompt)
        print("✅ Gemini 返回成功")
        return response.text.strip()
    except Exception as e:
        print("❌ Gemini 报错:", str(e))
        return f"调用 Gemini 失败：{str(e)}"
import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("models/gemini-pro", generation_config={"temperature": 0.7})

def get_health_advice(symptom: str) -> str:
    prompt = f"""
你是一位中文家庭医生，请根据以下症状提供简洁、实用的健康建议：

症状：{symptom}

要求：
- 用中文回答
- 建议包括：可能原因 + 初步应对措施 + 是否建议就医
- 使用简洁段落
"""
    try:
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        return f"调用 Gemini 失败：{str(e)}"
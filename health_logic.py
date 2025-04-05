# 📁 文件: medical_agent/health_logic.py
import os
import requests
from dotenv import load_dotenv

load_dotenv()
DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY")

def get_health_advice(symptom: str) -> str:
    return "建议多休息、多喝水、避免辛辣食物。"
    headers = {
        "Authorization": f"Bearer {DEEPSEEK_API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "deepseek-chat",
        "messages": [
            {"role": "system", "content": "你是一位中文家庭医生，提供简洁、温和的健康建议"},
            {"role": "user", "content": f"我最近的症状是：{symptom}。请给出初步建议"}
        ],
        "temperature": 0.7
    }

    try:
        response = requests.post(
            "https://api.deepseek.com/v1/chat/completions",
            headers=headers,
            json=data
        )
        response.raise_for_status()
        return response.json()["choices"][0]["message"]["content"]
    except Exception as e:
        return f"调用 DeepSeek 失败：{str(e)}"

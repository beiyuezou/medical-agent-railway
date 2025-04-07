import os
import requests
from dotenv import load_dotenv

load_dotenv()

DEESEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY")

def get_health_advice(symptom: str) -> str:
    print("🔍 正在使用 DeepSeek 分析症状:", symptom)

    url = "https://api.deepseek.com/v1/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {DEESEEK_API_KEY}"
    }
    payload = {
        "model": "deepseek-chat",
        "messages": [
            {
                "role": "system",
                "content": "你是一位中文医生，请根据症状提供简洁、实用的健康建议，建议要包含可能原因、建议措施、是否建议就医，分段返回。"
            },
            {
                "role": "user",
                "content": f"症状：{symptom}"
            }
        ],
        "temperature": 0.7
    }

    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        advice = response.json()["choices"][0]["message"]["content"]
        return advice.strip()
    except Exception as e:
        print("❌ DeepSeek 错误:", str(e))
        return f"调用 DeepSeek 失败：{str(e)}"
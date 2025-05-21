from fastapi import FastAPI
from pydantic import BaseModel
from openai import OpenAI
from dotenv import load_dotenv
import os

# .env 読み込み
load_dotenv()

# OpenAIクライアント初期化
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# FastAPIインスタンス作成
app = FastAPI()


# リクエストボディ用モデル
class ChatRequest(BaseModel):
    message: str
    user_id: int


# OpenAIとやり取りする関数
def get_chat_response(message: str) -> str:
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": message}],
    )
    return response.choices[0].message.content


# APIエンドポイント
@app.post("/chat")
async def chat(request: ChatRequest):
    reply = get_chat_response(request.message)
    return {"response": f"Hello User {request.user_id}, you said: {reply}"}

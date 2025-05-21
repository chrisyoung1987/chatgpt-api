# ChatGPT API with FastAPI + Docker + AWS EC2

## 概要
このプロジェクトは、FastAPI + Docker を使用し、OpenAI ChatGPT API と連携したチャットボットAPIサービスです。AWS EC2 上で動作可能です。

## 技術構成
- Python 3.10+
- FastAPI
- Docker
- OpenAI API (ChatGPT)
- AWS EC2

## 実行方法

### ローカル実行
uvicorn main:app --reload

### Docker 実行
docker build -t chatgpt-api .
docker run -p 8000:8000 --env-file .env chatgpt-api

### API エンドポイント
- `/chat`: POSTでメッセージ送信
- `/docs`: Swagger UI 自動生成

## .env ファイル例（アップロード禁止）
OPENAI_API_KEY=your_api_key_here

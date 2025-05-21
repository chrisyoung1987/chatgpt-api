# ベースイメージ（Python 3.10）
FROM python:3.10

# 作業ディレクトリ作成
WORKDIR /app

# requirements.txtをコピーして必要なパッケージをインストール
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# アプリのコードをコピー
COPY . .

# アプリの起動コマンド（開発用）
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

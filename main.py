# FastAPIをインポート
from fastapi import FastAPI

# FastAPIのインスタンス作成
app = FastAPI()

# GETメソッドでルートURLにアクセスされたときの処理
@app.get("/")
async def root():
    return {"message": "Hello World"}

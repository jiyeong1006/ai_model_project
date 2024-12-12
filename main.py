from fastapi import FastAPI
import redis

app = FastAPI()

# Redis 연결
r = redis.Redis(host="redis", port=6379, decode_responses=True)

@app.post("/set/{key}/{value}")
def set_key(key: str, value: str):
    r.set(key, value)
    return {"message": f"Key '{key}' set with value '{value}'"}

@app.get("/get/{key}")
def get_key(key: str):
    value = r.get(key)
    return {"key": key, "value": value}

@app.delete("/flush")
def flush_database():
    r.flushall()  # Redis 전체 데이터 삭제
    return {"message": "All data has been deleted from Redis."}
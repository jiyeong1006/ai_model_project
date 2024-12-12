import redis
from faker import Faker
import random

# Redis 연결 설정
redis_host = "redis"  # Docker Compose 서비스 이름
redis_port = 6379
r = redis.Redis(host=redis_host, port=redis_port, decode_responses=True)

# Faker 객체 생성
fake = Faker()

# ML용 데이터 생성 및 저장
for i in range(1, 10001):  # 10,000개의 데이터
    user_id = f"user_{i}"
    user_data = {
        "name": fake.name(),
        "age": random.randint(18, 80),
        "country": fake.country(),
        "email": fake.email(),
        "purchase_amount": round(random.uniform(10, 500), 2),
        "signup_date": str(fake.date_this_decade()),
    }
    # Redis에 저장 (Hash 형식)
    r.hmset(user_id, user_data)

print("ML용 데이터 입력이 완료되었습니다!")

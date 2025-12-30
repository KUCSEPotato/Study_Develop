# Request로 /hi 테스트
import requests
print("Testing /hi endpoint with requests...")
r = requests.get("http://localhost:8000/hi")
print(r.json())

# HTTPX로 테스트
# 교재에서는 비동기 호출시 사용
import httpx
print("Testing /hi endpoint with httpx...")
r = httpx.get("http://localhost:8000/hi")
print(r.json())
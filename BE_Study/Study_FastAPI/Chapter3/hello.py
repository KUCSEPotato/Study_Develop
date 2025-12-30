from fastapi import FastAPI

# app은 전체 웹 애플리케이션을 나타내는 최상위 FastAPI 객체다.
app = FastAPI()

@app.get("/hi") # 경로 데코레이터.
def greet(): # 경로 함수
    return {"Hello": "World"}

# uvicorn을 코드 내부에서 실행하는 로직
# 현재는 주석 처리
"""
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("hello:app", host="0.0.0.0", port=8000, reload=True) # reload -> 코드 변경 시 자동으로 웹 서버 재시작
"""

# uvicorn을 CLI에서 실행할 경우의 명령어
# uvicorn hello:app --host 0.0.0.0 --port 8000 --reload
# 경로 문제가 발생할 경우
# uvicorn Chapter3.hello:app --reload
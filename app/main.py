# fastapi 엔트리 포인트
# uvicorn 실행 명령어
# uvicorn app.main:app --reload --port 8000

from fastapi import FastAPI
import random
from app.question_main import questions, questions_cached

# 앱 인스턴스 생성
app = FastAPI()


# 루트 경로에 대한 핸들러
@app.get("/helloworld")
async def helloworld():
    return {"message": "Hello World"}


@app.post("/service")
async def service(difficulty: str, problem_type: str):
    """
    ### 함수 개발 순서: 입력-출력 값을 먼저 정의
    어떤 값을 받아서 어떤 값을 돌려줄지

    - 입력값:
        1. 난이도: ["상", "중", "하"]
        2. 문제 유형: ["품사 구분", "맞춤법", "띄어쓰기"]

    - 출력:
        난이도-문제유형 에 해당하는 문제 데이터
    """
    question_list = questions[difficulty][problem_type]
    question = random.choice(question_list)
    return {"id": question["id"], "문장": question["문장"], "보기": question["보기"]}


from pydantic import BaseModel


class Answer(BaseModel):
    id: int
    user_answer: str


@app.post("/service/answer")
async def answer(answer: Answer):
    id_ = answer.id
    answer_ = answer.user_answer
    for q in questions_cached:
        if q["id"] == id_:
            if q["정답"] == answer_:
                return {"id": id, "정답": True}
            else:
                return {"id": id, "정답": False}

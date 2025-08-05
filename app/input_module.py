def get_difficulty():
    print("난이도를 선택하세요: [상, 중, 하]")
    difficulty = input("난이도: ")
    if difficulty not in ['상', '중', '하']:
        print("잘못된 입력입니다. 기본값 '중'으로 진행합니다.")
        difficulty = '중'
    return difficulty

def get_problem_type(types):
    print("문제 유형을 선택하세요:", types)
    problem_type = input("유형: ")
    if problem_type not in types:
        print(f"잘못된 입력입니다. 기본값 '{types[0]}'으로 진행합니다.")
        problem_type = types[0]
    return problem_type

def get_answer():
    return input("정답을 입력하세요: ")
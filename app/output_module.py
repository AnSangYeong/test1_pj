def print_problem(problem_type, problem):
    if problem_type == "품사 구분":
        문장 = problem['문장']
        if '[' in 문장 and ']' in 문장:
            start = 문장.find('[') + 1
            end = 문장.find(']')
            target_word = 문장[start:end]
            clean_sentence = 문장.replace('[', '').replace(']', '')
        else:
            target_word = "(지시 단어 없음)"
            clean_sentence = 문장
        print(f"문장: {clean_sentence}")
        print(f'"{target_word}"의 품사는 무엇인가요?')
        for i, choice in enumerate(problem['보기'], 1):
            print(f"{i}. {choice}")
    elif problem_type == "맞춤법":
        print(problem['문장'])
    elif problem_type == "띄어쓰기":
        print("다음 문장을 올바르게 띄어쓰기 하시오:")
        print(problem['문장'])

def print_result(is_correct, correct_answer):
    if is_correct:
        print("정답입니다!")
    else:
        print(f"틀렸습니다. 정답은: {correct_answer}")
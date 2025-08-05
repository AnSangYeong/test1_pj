import importlib

input_mod = importlib.import_module('input_module')
output_mod = importlib.import_module('output_module')
question_mod = importlib.import_module('question_main')
answer_mod = importlib.import_module('answer_module')

def main():
    difficulty = input_mod.get_difficulty()
    types = question_mod.get_problem_types(difficulty)
    problem_type = input_mod.get_problem_type(types)
    problem = question_mod.get_problem(difficulty, problem_type)
    output_mod.print_problem(problem_type, problem)
    user_answer = input_mod.get_answer()
    is_correct = answer_mod.check_answer(user_answer, problem['정답'])
    output_mod.print_result(is_correct, problem['정답'])

if __name__ == "__main__":
    main()

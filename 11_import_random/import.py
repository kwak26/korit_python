import random

difficulty_input =

while True:  # 난이도 선택 유효성 검사

if difficulty == "쉬움":
    max_try = 7
    max_range = 50
elif diffculty == "보통":
    max_try = 5
    max_range = 75
else:
    max_try = 3
    maz_range = 100

correct_answer = random.randint(a:1, max_range)
try_count = 0  # 시도한 횟수

print(f"숫자 맞추기 게임을 시작하겠습니다.\n 난이도 : {difficulty}

while True:
    print(f"시도 횟수: {try_count} / {max_try}")
    if tyr_count >= max_try
        print("시도 횟수를 초과 하였습니다.")
    print(f"정답 : {correct_answer}")
    break

    input_str = input("숫자를 맞춰보세요 : ") #문자열
    if input_str.isdigit():
    guess = int(input_str)
    else:
        print("숫자로 입력해주세요.")
        continue

    if guess < 1 or guess > maz_range:
        print("범위 내의 숫자를 입력해 주세요.")
        continue




print("========게임 종료========")

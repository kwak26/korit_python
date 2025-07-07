#반복문 (for)
"""
for 변수 in 반복할대상:
    반복할코드
"""
from ctypes.wintypes import tagPOINT

#리스트 순회
fruits = ["사과", "바나나", "딸기", "포도"]

for fruit in fruits:
    print(fruit)

scores = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78
}
for key in scores: #키를 빼와서 변수에 할당
    print(key,"의 정수는", scores[key])

#튜플 순회
a_tuple = ("안녕", "하세요", "반갑습니다")
for a in a_tuple:
    print(a)

#세트 순회
a_set = {"사과", "바나나", "체리", "딸기", "오렌지"}
sorted_a_list = sorted(a_set)
for a in a_set:
    print(a)

#세트 정렬 추가 설명
numbers = {3, 1, 4, 1, 5, 9, 2}
sorted_numbers = sorted(numbers)
print(sorted_numbers)
print(type(sorted_numbers))

for num in range(1,10):
    if num == 5:
        continue
        print(num)

#실습문제
#1부타 100까지 짝수만 출력하기(range)
#for i in range1, 100):
#   if i % 2 == 0:
#   print(i)

for i in range(2, 101, 2):
    print(i)

#리스트이 합 구하기
numbers = [10, 20, 30, 40, 50]
total = 0

for num in numbers:
    total += num
print("리스트의 합:", total)

for dan in range(1, 10):
    for n in range(1, 10):
        print(f"{dan} x {n} = {dan * n}")

#평균구하기
scores = [80, 90, 75, 88, 92]
total = 0

for score in scores:
    total += score

average = total / len(scores)
print("평균점수:", average)

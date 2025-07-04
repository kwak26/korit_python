#딕셔너리
from tkinter.font import names

profile = {
    "이름": "곽동효",
    "나이": "41"}

#요소 접근
print(profile["이름"])

#요소 수정
profile["나이"] = 30
print(profile)


#요소 추가
profile["직업"] = "강사"
print(profile)

#요소 삭제
del profile["직업"]
print(profile)
# profile.clear() #전체삭제

#키만 불러오기
print(profile.keys())

#값만 불러오기
print(profile.values())

#키 값 둘다
print(profile.items())

python_grade = {
    "kelly": "B"
    "json" "A"}

print(sorted(python_grade.items())) #키 기준 오름차순 정렬
print(sorted(python_grade.items(), reverse=True)) #키 기준 내림차순 정렬

student = {}
#이름을 입력받고 해당 이르을 키로, 점수를 입력받고 값으로 추가
name = input("이름을 입력하세요 : ")
score = input(f"{name}의 점수를 입력하세요 : ")

#student = {"이동윤": 80}




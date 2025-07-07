#내장함수
#파이썬에서 기본적으로 지원하는 함수(Biult_in_Function
from gettext import dpgettext

#abs()
#숫자의 절댓값을 리턴하는 함수
print(abs(-10))
print(abs(-1,2))

#all()
#all(x)는 반복 가능한 데이터 x를 입력값으로 받으면
#이 x의 요소가 모두 참이면 True, 거짓이 하나라도 있으면 False를 리턴
#모든 요소가 참인가?
num_list = [1, 2, 0, 4]
print(all(num_list))
num_list = []
print(all(num_list))
#빈 리스트 같은 경우, 안에 어떤 요소도 존재하지 않는다.
#따라서 "거짓인 요소가 하나라도 있는가?" => "거짓인 요소가 없다"
#거짓인 요소가 없기 때문에 모든 요소가 참이라는 조건이 위배되지 않는다.


#any()
#ahy(x)는 반복 가능한 데이터 x를 입력값으로 받으면
#이 x의 요소가 하나라도 참이면 ture, 요소가 거짓이면 false
num_list = [1, 2, 0, 4]
print(any(num_list))
num_list = [0, 0, 0, 0]
print(any(num_list))

#chr()
#chr(i)는 유니코드를 넣으면 해당 문자로 리턴을 하는 함수
print(chr(97)) #a
print(chr(44032)) #가

#dir()
#객체가 지닌 변수나 함수를 보여주는 함수
name = "python"
print(dir(name))

#divmod(0
#2개의 숫자 a, b를 입력받고 그리고 a를 b로 나눈 몫과 나머지를
#튜플 형태로 리턴
print(divmod(7, 3))

#enumerate()
#순서가 있는 데이터(리스트, 튜플, 문자열)를 입력 받아서 인덱스 값을
#포함하는 enumerate객체를 리턴
#인덱스와 값을 두개의 변수로 언팩
a_list = ["name", "age", "birth"]

for i, value in enumerate(a_list):
    print(i, value)

#eval()
#문자열로 구성되어 있는데 해당 문자열을 실행한 값
a_str = "1 + 2"
print(eval(a_str))
print(eval("divmod(7,2"))

#filter()
#첫 번째 인수로 함수, 두 번째 인수로 반복가능한 데이터
#그리고 반복가능한 데이터의 요소 순서대로 함수를 홀출했을 때
#리턴값이 참인것만 묶어서 리턴
def posigive(x):
    return x > 0

print(list(filter(posigive, [1, -2, 5, -3, 8])))

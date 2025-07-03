#입력받기
#input()
# a = input()
# print("내가 입력한 것: " + a)

# username = input("이름을 입력하세요 : ")
# print("사용자 이름 : " + username)

# age = input("나이를 입력하세요 : ")
# print(type(age))
# print("사용자 나이 : " + age)
# #input()으로 입력 받은 모든 값은 문자열 형태이다.

#출력하기 다양한 방식
Last_name = "곽"
first_name ="동효"
name = Last_name + first_name
age = 41 #int
phone_number = "01020520915" #숫자는 맨 앞이 0이 나올 수 없음
# print("hi" + "hello" + "world")
# print("hi", "hello", "world")
# print("내 전화번호는 " + phone_number+"입니다")
# print("제 나이는 " + age + "입니다.")
# print("제 나이는 {}입니다.".format(age))
# print("제 이름은 {}, 나이는 {}입니다.".format(name,age))
# print("제 이름은 {nm}, 나이는 {ag}입니다.".format(nm="홍길동", ag=18))

# print(f"제 나이는 {age} 입니다.") #f-string 방식

# print("제 나이는 %s 입니다."% age) #모든 문자를 문자열로 포맷팅해서 출력
# print("제 나이는 %d입니다." % age)#모든 문자를 정수형로 포맷팅해서 출력
# print("제 이름은 %s 이고, 제 나이는 %d 입니다." "%(name, age))
# print("loading...%d%%" % 98)
print("%10s" % "hi")#문자열 앞에 공백 포함)
print("%-10s" % "hello") #문자열 포함 길이(문자열 뒤에 공백 포함)
print("%0.4f" % 3.422134) #앞의 0은 자릿수를 의미, .4는 소수점 4번째 자리까지 표현
print("%10.4f" % 3.422134)#10은 자리수를 의미하므로 소수점 4번째 자리만큼 앞에 공백

"""
%s => 문자열
%c => 문자 1개
%d => 정수
% => 실수
%o => 8진수
%x => 16진수
%% => 리터럴 (문자

#실습
#이름:"곽동효"
#나이:"41"
#취미:"운동"
#주소:"부산시 기장군 정관3로51"
#각각 변수에 넣고 f-string 방식으로 출력
#ex)제 이름은 ***이고 나이는 **살 입니다. 제 취미는 ***이고 주소는 ***입니다.

print("제 나이는 %s 입니다."% age)
name = input("이름:")
age=input("나이:")
hobby=input("취미:")
adress=input("주소:")
print("제 이름은 {name}이고 나이는 {age} 입니다. 제 취미는 {hobby}이고 주소는 {adreess}입니다.")
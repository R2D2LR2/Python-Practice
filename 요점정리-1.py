######################################################
# 숫자처리 함수

# print(abs(-5))
# print(pow(4, 2))  # 4^2
# print(max(5, 12))  # 12
# print(min(5, 12))  # 5
# print(round(3.14))  # 3
# print(round(4.99))  # 5

# from math import *
# print(floor(4.99))  # 내림 4
# print(ceil(3.14))  # 올림 4
# print(sqrt(16))  # 제곱근

######################################################
# 랜덤함수
from random import *
print(random())  # 0.0 ~ 1.0 미만 난수
print(random() * 10)  # 0.0 ~ 10.0 미만 난수
print(int(random() * 10))  # 0.0 ~ 10.0 미만 난수를 정수로
print(randrange(1, 5))  # 1 ~ 5 미만 난수를 정수로
print(randint(1, 5))  # 1 ~ 5 이하의 난수를 정수로

######################################################
# 슬라이싱
jumin = "990120-1234567"

print("성별 : " + jumin[7])
print("연 : " + jumin[0:2])  # 0부터 2직전까지
print("월 : " + jumin[2:4])
print("일 : " + jumin[4:6])
print("생년월일 : " + jumin[:6])  # 처음부터 6 직전까지
print("뒤 7자리 : " + jumin[7:])  # 7부터 끝까지
print("뒤 7자리(뒤에부터) : " + jumin[-7:-1])  # 맨뒤에서 끝부터 7번째까지


######################################################
# 문자열 처리
python = "Python is Amazing"
print(python.lower())
print(python.upper())
print(python[0].isupper())
print(len(python))
print(python.replace("Python", "Java"))

index = python.index("n")  # n의 위치 반환
print(index)
index = python.index("n", index + 1)  # n 글자 중 두 번째 n의 위치를 반환
print(index)

print(python.find("Java"))  # 찾는 값이 없으면 -1을 반환
# print(python.index("Java"))  # 찾는 값이 없으면 오류가 발생하면서 프로그램 폴트
print(python.count("n"))  # 문자 개수

######################################################
# 문자열 표현 방법
print("a" + "b")
print("a", "b")

# 방법 1
# 정수만 입력
print("나는 %d살 입니다." % 20)
# String
print("I like %s." % "python")
# Character
print("Apple 은 %c로 시작합니다." % "A")

print("나는 %s색과 %s색을 좋아해요." % ("파란", "빨간"))

# 방법 2
print("나는 {}살입니다." .format(20))
print("나는 {}색과 {}색을 좋아해요." .format("파란", "빨간"))
print("나는 {1}색과 {0}색을 좋아해요." .format("파란", "빨간"))

# 방법 3
print("나는 {age}살이며, {color}색을 좋아해요.".format(age=20, color="빨간"))

# 방법 4 (v3.6 이상)
age = 20
color = "빨간"
print(f"나는 {age}살이며, {color}색을 좋아해요.")

######################################################
# \n 줄바꿈
print("백문이 불여일견 \n 백견이 불여일타")
# \" \' 문장 내에서 큰따옴표 및 작은 따움표 표기
print("저는 \"나도코딩\" 입니다.")
# \\ 문장 내에서 \ 표기
print("C:\\Users\\Zin\\Dropbox\\Python Practice")
#  \r 커서를 맨 앞으로 이동
print("red apple\rpine")
# \b 한글자 삭제
print("redd\bapple")
# \t 탭
print("redd\tapple")

######################################################
# 리스트 (자료형에 구애받지 않고 사용가능)
subway = ["유재석", "조세호", "박명수"]
print(subway)

# 조세호가 몇 번재 칸에 타고 있는가?
print(subway.index("조세호"))
# 하하가 다음정류장에서 마지막 칸에 탑승
print(subway.append("하하"))
# 정형돈을 유재석 / 조세호 사이에 태움
print(subway.insert(1, "정형돈"))
# 지하철에 앉아 있는 사람을 한 명씩 뒤에서부터 내림
print(subway.pop())
# 같은 이름의 사람이 몇 명 있는지 확인
subway.append("유재석")
print(subway.count("유재석"))

# 정렬 오름차순
num_list = [5, 2, 4, 3, 1]
num_list.sort()
# 정렬 내림차순
num_list.reverse()
# 리스트 안의 데이터 지우기
num_list.clear()

# 리스트 합치기
num_list = [5, 2, 4, 3, 1]
mix_list = ["안녕하세요", 20, True]
num_list.extend(mix_list)

######################################################
# 사전
cabinet = {3: "유재석",
           100: "김태호"}
print(cabinet[3])  # key에 해당하는 값이 없으면 오류
print(cabinet.get(30))  # key에 해당하는 값이 없으면 none 출력
print(cabinet.get(5, "사용가능"))  # key에 해당하는 값이 없으면 "사용가능" 문자 출력

print(3 in cabinet)  # key가 변수안에 있으면 Treu, 없으면 False 출력
cabinet["C-20"] = "조세호"  # 사전에 key와 값을 저장, key 가 이미 존재하면 해당 값으로 update

del cabinet["C-20"]  # 해당 키와 값을 삭제
# 키 들만 출력
print(cabinet.keys())
# 값 들만 출력
print(cabinet.values())
# 키와 값을 모두 출력
print(cabinet.items())
# 사전자료 비우기
cabinet.clear()

######################################################
# 튜플 (리스트와 같으나 내용 변경이나 추가가 불가하나 속도가 빠름)

menu = ("돈까스", "치즈까스")
print(menu[0])
print(menu[1])

######################################################
# 셋트 (중복이 안되고 순서가 없다 집합관계를 설정할 수 있다)
my_set = {1, 2, 3, 3, 3}
print(my_set)  # 3은 하나만 출력됨

java = {"유재석", "김태호", "양세형"}
python = set(["유재석", "박명수"])

# 교집합
print(java & python)
print(java.intersection(python))
# 합집합
print(java | python)
print(java.union(python))
# 차집합
print(java - python)
print(java.difference(python))
# 추가
python.add("김태호")
# 제거
java.remove("김태호")

######################################################
# 자료구조의 변경
menu = {"커피", "우유", "주스"}
print(menu, type(menu))  # 자료형 확인

menu = list(menu)  # 셋트 -> 리스트
menu = tuple(menu)  # 셋트 -> 튜플
menu = set(menu)  # 튜플 -> 셋트

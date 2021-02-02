######################################################
# 조건문 if
# weather = input("오늘 날씨는 어때요? ")
# if weather == "비" or weather == "눈":
#     print("우산을 챙기세요")
# elif weather == "미세먼지":
#     print("마스크를 챙기세요")
# else:
#     print("준비물 필요 없어요")

# temp = int(input("기온은 어때요?"))
# if 30 <= temp:
#     print("너무 더워요. 나가지 마세요")
# elif 10 <= temp and temp < 30:
#     print("괜찮은 날씨에요")
# elif 0 <= temp < 10:
#     print("외투를 챙기세요")
# else:
#     print("너무 추워요. 나가지 마세요")

######################################################
# 조건문 for
# for waiting_no in [0, 1, 2, 3, 4]:  # range(1,5)
#     print("대기번호 : {0}".format(waiting_no))

# starbucks = ["아이언맨", "토르", "아이엠 그루트"]
# for customer in starbucks:
#     print("{0}님, 커피가 준비되었습니다".format(customer))

######################################################
# 조건문 while (조건이 만족할 때 까지 반복)
# customer = "토르"
# index = 5
# while index >= 1:
#     print("{0}, 커피가 준비 되었습니다. {1} 번 남았어요.".format(customer, index))
#     index -= 1
#     if index == 0:
#         print("커피는 폐기처분 되었습니다.")

# customer = "아이언맨"
# index = 1
# while True:
#     print(f"{customer}, 커피가 준비되었습니다. 호출{index}회") #무한 반복
#     index += 1
# customer = "토르"
# person = "Unknown"
# while person != customer:
#     print(f"{customer}, 커피가 준비되었습니다.")
#     person = input("이름이 어떻게 되세요 ")

######################################################
# continue 조건에 맞으면 아래 실행문을 실행하지 않고 다음 반복문으로 넘어감
# break 조건에 맞으면 아래 실행문을 실행하지 않고 반복문을 빠져나감

# absent = [2, 5]  # 결석
# no_book = [7]
# for student in range(1, 11):  # 1~10
#     if student in absent:
#         continue
#     elif student in no_book:
#         print(f"오늘 수업 여기까지. {student}는 교무실로 따라와")
#         break
#     print(f"{student}, 책을 읽어봐")

######################################################
# 한줄 for

# 출석번호가 1,2,3,4, 앞에 100을 붙임 -> 101, 102, 103, 104
# students = list(range(1, 5))
# print(students)
# students = [i+100 for i in students]
# print(students)

# 학생이름 길이로 변환 및 대문자 변환
students = ["Iron Man", "Thor", "I am groot"]
len_students = [len(i) for i in students]
print(len_students)
upper_students = [i.upper() for i in students]
print(upper_students)

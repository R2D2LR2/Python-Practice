# 당신은 코코아 서비스를 이용하는 택시 기사님 입니다.
# 50명의 승객과 매칭 기회가 있을 때, 총 탑승 승객 수를 구하는 프로그램을 작성하세요.
#
# 조건1 : 승객별 운행 소요 시간은 5~50분 사이의 난수로 정해진다.
# 조건2 : 당신은 소요 시간 5~15분 사이의 승객만 매칭해야 한다.
#
# (출력문 예제)
# [O] 1번째 손님 (소요시간 : 15분)
# [ ] 2번째 손님 (소요시간 : 50분)
# [ ] 3번째 손님 (소요시간 : 20분)
# [O] 4번째 손님 (소요시간 : 5분)
# ...
# [ ] 50번째 손님 (소요시간 : 15분)
# 총 탑승 승객 : 2 분

from random import *

index = 1
chk_cnt = 0
while index <= 50:
    random_time = int(randint(5, 50))  # 5 ~ 50 이하 난수를 정수로
    if 5 <= random_time <= 15:
        chk = "O"
        chk_cnt += 1
    else:
        chk = " "
    print(f"[{chk}] {index}번째 손님 (소요시간 : {random_time}분")
    index += 1
print(f"총 답승 승객 : {chk_cnt} 분")

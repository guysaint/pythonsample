'''
슬라이딩 윈도우와 투포인트를 사용한 최근 매출 데이터 추출하기
1. 날짜와 요일 매출금액 순으로 입력한다.
(날짜와 요일은 최초만 입력하고 두번째 입력부터는 매출 금액만 입력한다.)
2. 메뉴에서 원하는 기능을 선택한다.
'''
from datetime import datetime, timedelta

sales_data = {}

print("🔸 첫 줄은 날짜 요일 금액을 입력하세요 (예: 2025-07-01 화 120)")
print("🔸 그다음부터는 금액만 입력하면 날짜와 요일은 자동으로 채워집니다.")
print("🔸 빈 줄을 입력하면 종료됩니다.\n")

# 요일 이름 매핑
weekdays = ["월", "화", "수", "목", "금", "토", "일"]

# 초기 입력
first_line = input("> ").strip()
date_str, day_str, amount = first_line.split()
sales_data[date_str] = {"요일": day_str, "매출": int(amount)}

# 날짜 계산용 시작일
current_date = datetime.strptime(date_str, "%Y-%m-%d")
current_weekday_index = weekdays.index(day_str)

# 반복 입력
while True:
    line = input("> ").strip()
    if not line:
        break

    try:
        current_date += timedelta(days=1)
        current_weekday_index = (current_weekday_index + 1) % 7
        date_key = current_date.strftime("%Y-%m-%d")
        sales_data[date_key] = {
            "요일": weekdays[current_weekday_index],
            "매출": int(line)
        }
    except ValueError:
        print("숫자(매출 금액)만 입력해주세요.")

# 결과 확인
print("\n입력 완료! 총", len(sales_data), "건")
# 날짜 순으로 정렬
sales_list = sorted(sales_data.items())  # [(날짜, {"요일":, "매출":})]

#분석 기능
# 슬라이딩 윈도우
def sliding_window(days, start_index=0):
    if start_index + days > len(sales_list):
        print("범위를 벗어났습니다.")
        return
    
    window = sales_list[start_index:start_index+days]
    total = sum(entry[1]['매출'] for entry in window)
    print(f"\n조회 결과(시작일: {window[0][0]}):")
    for date, info in window:
        print(f"{date} ({info['요일']}) - {info['매출']}원")
    print(f"합계:{total}원\n")
        
# 투 포인트        
def top_two_sales():
    if len(sales_list) < 2:
        print("데이터가 부족합니다 (최소 2개 필요)")
        return

    # 초기 top1, top2는 sales_list의 첫 2개를 기준으로 설정
    if sales_list[0][1]['매출'] >= sales_list[1][1]['매출']:
        top1 = sales_list[0]
        top2 = sales_list[1]
    else:
        top1 = sales_list[1]
        top2 = sales_list[0]

    # 인덱스 2부터 끝까지 순회하며 최고/차고 매출 갱신
    for i in range(2, len(sales_list)):
        current = sales_list[i]
        current_amount = current[1]['매출']

        if current_amount > top1[1]['매출']:
            top2 = top1
            top1 = current
        elif current_amount > top2[1]['매출']:
            top2 = current

    # 결과 출력
    print("\n최고 매출 TOP 2 (투 포인터 방식):")
    print(f"1위: {top1[0]} ({top1[1]['요일']}) - {top1[1]['매출']}원")
    print(f"2위: {top2[0]} ({top2[1]['요일']}) - {top2[1]['매출']}원\n")
    
while True:
    print("분석 옵션을 선택하세요:")
    print("1. 최근 N일 매출 합 (슬라이딩 윈도우)")
    print("2. 특정 시작일부터 M일간 매출 합 (슬라이딩 윈도우)")
    print("3. 최고 매출 TOP 2 날 (투 포인터)")
    print("4. 입력한 데이터 확인하기")
    print("0. 종료")

    choice = input("선택: ").strip()

    if choice == "1":
        n = int(input("최근 N일: "))
        sliding_window(n, start_index=len(sales_list)-n)

    elif choice == "2":
        start_date = input("시작 날짜 (예: 2025-07-01): ").strip()
        m = int(input("기간(일 수): "))
        start_idx = next((i for i, (date, _) in enumerate(sales_list) if date == start_date), -1)
        if start_idx == -1:
            print("해당 날짜를 찾을 수 없습니다.")
        else:
            sliding_window(m, start_index=start_idx)

    elif choice == "3":
        top_two_sales()
    
    elif choice == "4":
        for date, info in sales_data.items():
            print(f"{date} ({info['요일']}) - {info['매출']}원")

    elif choice == "0":
        print("종료합니다.")
        break

    else:
        print("올바른 메뉴를 선택하세요.")    

    
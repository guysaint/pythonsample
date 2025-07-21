#자판기 메뉴 (딕셔너리 사용)
menu = {"1":{"name":"아메리카노", "price":2500},
        "2":{"name":"카페라떼", "price":3000},
        "3":{"name":"아이스티","price":3200},
        "4":{"name":"레모네이드", "price":3800}}

#음료 출력 함수
def show_menu():
    print("******* 메 뉴 *******")
    #딕셔너리의 key, value를 튜플로 가져오기
    for key, value in menu.items():
        print(key+". "+value["name"]+' '+str(value["price"])+"원")
    print("0. 종료")
    print("*"*20)
    

def vending_machine():
    while True:
        show_menu()
        choice = input("원하시는 메뉴의 숫자를 입력하세요: ")

        if choice == "0":
            print("안녕히 가세요")
            break
        
        elif choice in menu:  # 유효한 메뉴 번호일 때만 처리
            drink = menu[choice]["name"]
            price = menu[choice]["price"]
            print("😄"+drink+"를 선택하셨습니다. 가격:"+str(price)+"원")

            try:
                money = int(input("투입할 금액을 입력해주세요: "))
            except ValueError:
                print("숫자만 입력해주세요.")
                continue

            if money == price:
                print(drink + "를 드리겠습니다. 감사합니다.")
            elif money > price:
                print(drink + "와 " + str(money - price) + "원을 드립니다. 감사합니다. 또 오세요~😍")
            else:
                total = price - money
                print("금액이 부족합니다.", str(total) + "원을 더 투입하세요.")
                while total > 0:
                    try:
                        addmoney = int(input("추가 금액투입하세요: "))
                    except ValueError:
                        print("숫자만 입력해주세요.")
                        continue
                    total -= addmoney
                    if total > 0:
                        print("금액이 부족합니다. " + str(total) + "원을 더 투입하세요.")
                if total == 0:
                    print(drink + "를 드리겠습니다. 감사합니다.")
                else:
                    print(drink + "와 " + str(-total) + "원을 드립니다. 감사합니다. 또 오세요~😍")
        else:
            print("😅잘못 입력하셨습니다. 다시 선택해주세요.")

          
vending_machine()

'''
def tal():
    total=price-money
    print("금액이 부족합니다.",str(total)+"원을 더 투입하세요.")
    addmoney=int(input("추가 금액투입하세요."))
    if addmoney>total:
        print(drink+"와",str(addmoney-total)+"원을 드립니다. 감사합니다. 또 오세요~😍")
    while addmoney<total:
        print("금액이 부족합니다.",str(total-addmoney)+"원을 더 투입하세요.")
        total=total-addmoney
        addmoney=int(input("추가 금액투입하세요."))
        if addmoney>total:
            print(drink+"와",str(addmoney-total)+"원을 드립니다. 감사합니다. 또 오세요~😍")
        elif addmoney==total:
            print(drink+"를 드리겠습니다. 감사합니다.")
'''
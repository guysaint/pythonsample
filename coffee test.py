#자판기 메뉴 (딕셔너리 사용)
menu = {"1":{"name":"아메리카노", "price":2500},
        "2":{"name":"카페라떼", "price":3000},
        "3":{"name":"아이스티","price":3200},
        "4":{"name":"샷추가", "price":500}}

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
        choice=input("원하시는 메뉴의 숫자를 입력하세요.")
        drink = menu[choice]["name"]
        price = menu[choice]["price"]
        if choice==0:
            print("안녕히 가세요.")
            break
        elif choice not in menu.keys():
            print("😅잘못입력하셨습니다. 다시 선택해주세요.")
            continue
        elif choice=="1":
            print("😄"+drink+"를 선택하셨습니다. 가격:"+str(price)+"원")
            money=int(input("투입할 금액을 입력해주세요."))
            if money==price:
                print(drink+"를 드리겠습니다. 감사합니다.")
                continue
            elif money>price:
                print(drink+"와",str(money-price)+"를 드립니다. 감사합니다. 또 오세요~😍")
            elif money<price:
                total=price-money
                print("금액이 부족합니다.",str(total)+"를 더 투입하세요.")
                addmoney=int(input("추가 금액투입하세요."))
                if addmoney>total:
                    print(drink+"와",str(addmoney-total)+"를 드립니다. 감사합니다. 또 오세요~😍")
                while addmoney<total:
                    
                    print("금액이 부족합니다.",str(total-addmoney)+"를 더 투입하세요.")
                    total=total-addmoney
                    addmoney=int(input("추가 금액투입하세요."))
                    if addmoney==total:
                        print(drink+"를 드리겠습니다. 감사합니다.")
                    
        
        
        
        
vending_machine()
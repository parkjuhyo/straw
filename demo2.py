def Menu():
    print("""
+---------------------[메뉴]---------------------+
| 1. 아메리카노/ 1000원 2.에스프레소/ 1000원 |
| 3. 카페라떼/ 600원 4. 바닐라라뗴 650원 |
| 5. 카페모카/ 700원 6.달고나라떼 / 750원 |
| 7. 주문다시(reset) 8. 주문종료(exit) |
+--------------------------------------------------+
""")
def order(money, order):
    changes= 0
    
    if order == 1:
        print("아메리카노를 주문하셨습니다.")
        changes= money - 1000
    elif order == 2:
        print("에스프레소를 주문하셨습니다.")
        changes= money - 1000
    elif order == 3:
        print("카페라뗴를 주문하셨습니다.")
        changes= money - 600
    elif order == 4:
        print("바닐라라떼를 주문하셨습니다.")
        changes = money - 650
    elif order == 5:
        print("카페모카을 주문하셨습니다.")
        changes = money - 700
    elif order == 6:
        print("달고나라떼를 주문하셨습니다.")
        changes = money - 750
    if changes < 0: 
        print("남은 금액(", changes - money,"원)이모자랍니다." ) #돈이 모자랄떄 돈 추가로 입력받아야함
        add_money = int(input(" 돈을 추가하세요."))
        money += add_money
        changes += add_money

    print("남은 금액은 ", changes," 원입니다.") #남은금액 출력
    return changes
def screen():
    print(" ************ 전주대 자판기 프로그램 ************ ")
    # Menu()
    money = int(input("금액을 입력하시오=>"))
    menu = int(input("메뉴를 선택하시오=>"))
    return money, menu
def main():
    money, menu = screen()
    while True:
        if menu >=1 and menu <=6: # 음료수를 구매한 경우
            money = order(money, menu)
            Menu()
        elif menu == 7: # 주문을 리셋한 경우
            Menu()
            money = int(input("금액을 다시 입력하시오=>"))
        elif menu == 8: #  주문종료를 누르면, 주문을 종료하고 잔액을 반환한다.
            print("남은 금액은 ", money, " 원입니다." "이용해주셔서 감사합니다.")
            break
        else :  # 주문을 잘못 입력하면, 다시 주문을 받는다.
            print("메뉴를 잘못 입력하였습니다.")
        # money = int(input("금액을 입력하시오=>"))
        menu = int(input("메뉴를 선택하시오=>"))

if __name__ == '__main__':
    main()
    



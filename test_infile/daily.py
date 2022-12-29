# 일일 매출 기록 파일 이름과 결산 파일 이름을 지정하고 연다.
daily_sale_file = open('sales.txt', 'w+', encoding='utf-8')
summary_file = open('summary.txt', 'w', encoding='utf-8')
sales_cnt = 0
sales_sum = 0
# 일일 매출을 입력받아 파일에 쓴다.
while True:
    sale_day = input('매출날짜를 입력하시오(형식: YY-MM-DD)')
    sale = input('매출액을 입력하시오.')
    if sale_day == '' or sale == '': # null 값이면 종료
        break
    else:
        daily_sale_file.write(sale_day + ' ' + sale + '\n')
        sales_cnt += 1
        sales_sum += int(sale)
        # 총매출과 일평균 매출을 결산 파일에 기록한다.
        summary_file.write("총매출 = " + str(sales_sum) + "\n")
        summary_file.write("평균 일매출 = " + str(sales_sum/sales_cnt))
daily_sale_file.close()
summary_file.close()
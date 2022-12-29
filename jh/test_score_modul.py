# ----- 성적 입력 -----
def Insert(student):
    name = input('이름 입력 : ')

    #이름이 딕셔너리 내에 없을경우,
    if (name not in student) == True:

        #성적 입력
        kor =  int(input('국어 성적을 입력하세요 : '))
        eng =  int(input('영어 성적을 입력하세요 : '))
        math = int(input('수학 성적을 입력하세요 : '))
        print('성적이 입력되었습니다.')

        score = kor+eng+math
        avg = round(score/3, 3)

    #이름이 중복일 경우
    else:
        print('학생이 존재합니다.')
        return Insert(student)
        

    #딕셔너리 Key = Value
    student[name] = [kor, eng, math, score, avg]
    return student


# ----- 성적 출력 -----
def View(student):
    print("=======================================================")
    print('점수 : [국, 영, 수, 총점, 평균]')

    
    # 딕셔너리 key, value 출력하기(item)
    for key, value in student.items():
        print(key,':', value)
    print("=======================================================")
        
    return student


# ----- 학생 검색 -----
def Search(student):
    search_name = input('검색할 학생의 이름을 입력해주세요 : ')
    
    # 검색한 이름이 딕셔너리내의 Key값과 일치하는 경우
    if(search_name in student) == True:
        print("=======================================================")
        print('점수 : [국, 영, 수, 총점, 평균]')
        print(search_name,':' , student.get(search_name),' ')                   
        print("=======================================================")

    else:
        print('해당 이름이 없습니다.')
        print('다시 검색하시려면 1번, 메인 화면으로 돌아가시려면 2번을 눌러주세요.')
        num = int(input('번호 입력 : '))
        if num ==1:
            Search(student)
        else:
            create()

    return student

    
# ----- 성적 수정 -----
def Update(student):
    update_name = input('수정할 학생의 이름을 입력해주세요 : ')

    # 검색한 이름이 딕셔너리내의 Key값과 일치하는 경우
    if(update_name in student) == True:
        print('국어 영어 수학 성적 입력 :')

        #국, 영, 수 성적 입력(덮어씀)
        kor, eng, math = map(int, input().split())

        score = kor+eng+math
        avg = round(score/3, 3)

        #딕셔너리내의 Key = Value
        student[update_name] = [kor, eng, math, score, avg]
        person = student[update_name]

    else:
        print('해당 이름이 없습니다.')
        print('수정할 학생의 이름을 다시 입력하시려면  1번, 메인 화면으로 돌아가시려면 2번을 눌러주세요.')
        num = int(input('번호 입력 : '))
        if num ==1:
            Update(student)
        else:
            create()

    return student


# ----- 학생 삭제 -----
def Delete(student):
    delete_name = input('삭제할 학생의 이름을 입력해주세요 : ')

    # pop(키) - 특정 키-값 쌍을 삭제
    if(delete_name in student) == True:
        student.pop(delete_name)

    return student      


def create():
    while True:
        select = int(input("1.입력 2.출력 3.검색 4.수정 5.삭제 6.종료 \n"))

        # ----- 성적 입력 -----
        if select == 1:
            student = Insert(student)

        # ----- 성적 출력 -----
        elif select ==2:
            student = View(student)

        # ----- 학생 검색 -----
        elif select == 3:
            student = Search(student)

        # ----- 학생 수정 -----
        elif select == 4:
            student = Update(student)

        # ----- 학생 삭제 -----
        elif select == 5:
            student = Delete(student)
        else:
            print("종료되었습니다.")
            break

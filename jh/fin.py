import pw, test_score_modul #pw와 test_score_modul를 불러오기

id = input("아이디를 입력하시오") 
print(id,pw.password()) #입력한 아이디와 랜덤생성한 비밀번호 같이 출력

mode = input("관리자와 학생 선택")
student = dict()#student 딕셔너리 생성
if mode == '관리자': 
    while True:
        print("1.성적입력 2. 성적출력 3.학생검색 4. 성적수정 5.학생삭제 6.멈춤") 
        mm = int(input("메뉴 선택"))
        if mm == 1:
            test_score_modul.Insert(student)
        if mm == 2: 
            test_score_modul.View(student)
        if mm == 3:
            test_score_modul.Search(student)        
        if mm == 4:
            test_score_modul.Update(student)
        if mm ==5:
            test_score_modul.Delete(student)
        if mm == 6:
            break
elif mode == '학생':
    test_score_modul.View(student)
    
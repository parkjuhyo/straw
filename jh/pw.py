#비밀번호 생성 모듈

def password():
    import string
    import random
    
    new_pw_len = 10 # 새 비밀번호 길이
    
    # print("영어대소문자", string.ascii_letters)
    # print("숫자", string.digits)
    # print("특수문자", string.punctuation)
    
    pw_candidate = string.ascii_letters + string.digits + string.punctuation 
    
    new_pw = ""
    for i in range(new_pw_len):
        new_pw += random.choice(pw_candidate)
    
    return new_pw
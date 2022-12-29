infile = open("test_infile/friends.txt", "r", encoding='utf-8')
s = infile.read(10) # 10개의 문자 읽어오기
print(s)
infile.close() 
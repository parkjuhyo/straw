infile = open("test_infile/friends.txt", "r", encoding='utf-8')
s = infile.readline() # 한 줄 읽기
print(s)
s = infile.readline() # 한 줄 읽기
print(s)
s = infile.readline() # 한 줄 읽기
print(s)
infile.close() 
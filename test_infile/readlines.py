infile = open("test_infile/friends.txt", "r", encoding='utf-8')
lines = infile.readlines() # 파일의 모든 줄 읽기
print(lines)
for line in lines:
    print(line.rstrip())
infile.close() 
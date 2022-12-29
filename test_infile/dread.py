infile = open("test_infile/friends.txt", "r", encoding='utf-8')
for line in infile:
# 읽어올 때, 오른쪽 공백문자(\n) 제거
    line = line.rstrip()
    print(line)
infile.close() 
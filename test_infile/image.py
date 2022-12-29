file1 = input("원본 파일 이름: ")
file2 = input("복사 파일 이름: ")
f=open('test_infile/'+file1,'rb')
h=open('test_infile/'+file2,'wb')
bufsize=1024
while True:
    buffer_data = f.read(bufsize)
    if not buffer_data:
        break
    h.write(buffer_data)
h.close()
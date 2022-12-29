import os.path
if os.path.isfile("test_infile/prices.txt"):
    print("동일한 이름의 파일이 이미 존재합니다. ")
else:
    outfile = open("prices.txt", "w", encoding='utf-8')
    outfile.write("사과 5000\n")
    outfile.write("배 7000\n")
    outfile.write("포도 9000\n")
    outfile.close()
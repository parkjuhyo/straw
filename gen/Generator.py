def file_read():
    with open(open('gen','r', encoding='UTF-8')) as file:
        while True:
            line = file.readline()
            if line == '':
                break
            yield line.strip('\n')                    
for i in file_read():
    print(i)
file = open('C:\\temp\\test.txt', 'r')
for line in file:
    print(line)
file.close()
file = None
fso = None
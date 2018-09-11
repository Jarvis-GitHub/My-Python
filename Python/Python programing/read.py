file1 = open('c:/Users/Jarvis/Desktop/a.txt', encoding='UTF-8')
a = file1.readlines()
file2 = open('c:/Users/Jarvis/Desktop/b.txt', mode='r+', encoding='UTF-8')
b = file1.readlines()
for i in a:
    j = i.split()
    file2.writelines(f"{j[1]} {j[0]}\n")

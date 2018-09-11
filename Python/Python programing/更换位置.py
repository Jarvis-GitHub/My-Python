print("请拖入待处理文件：")
file1_path = input('>')
file1 = open(file1_path)

print("请拖入待写入文件：")
file2_path = input('>')
file2 = open(file2_path)

from_file = file1.read()
to_file = file2.read()

for i in from_file:
    print(i)

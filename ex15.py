from sys import argv

script, filename = argv
#在命令行输入运行的脚本，以及文件名
#filename = input("请输入文件名：")
txt = open(filename)

print(f"Here's your file {filename}:")
print(txt.read())
txt.close() #这个东西尤为重要

print("Type the filename again:") #这里面的filename会被替换
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read())
txt_again.close()

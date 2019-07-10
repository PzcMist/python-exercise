from sys import argv   #这个就是为了能在命令行这直接输出

script, input_file = argv

def print_all(f):
    print(f.read())   #就是读出txt中所有的文字

def rewind(f):
    f.seek(0)    #这个意思就是，从头开始

def print_a_line(line_count, f):
    print(line_count, f.readline())  #这是打印出一行

current_file = open(input_file)   #这里是将文件赋值给current_file这个参数

print("First let's print the whole file:\n")

print_all(current_file)

print("Now let's rewind, kind of like a tape.")

rewind(current_file)
#如果没有这个的话，那么在执行下面代码时，就不能打印出文档的三段
#所以这个函数调用的目的就是为了使指针重新回到文档的开头

print("Let's print three lines:")
current_line = 0
while current_line <= 2:
    current_line += 1
    print_a_line(current_line, current_file)
#其实在这里，调用了readline方法（会返回一个\n；加上print函数本身就自带\n，所以在
#显示中会发现行与行之间有空格）


#以下的是第二种实现方法
#current_line = 1
#print_a_line(current_line, current_file)  #current_line的值为1， 第一段

#current_line = current_line + 1
#print_a_line(current_line, current_file)
#current_line的值为2，把值传给print_a_line()这个函数的第一个参数， 第二段

#current_line = current_line + 1
#print_a_line(current_line, current_file)  #current_line的值为3， 第三段

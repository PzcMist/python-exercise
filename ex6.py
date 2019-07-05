type_of_people = 10
#变量名为type_of_people，同时它的值为10
x = f"There are {type_of_people} type of people."

binary = "binary"
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}."

print(x)
print(y)

print(f"I said:{x}")
#在这里第一个f是对{x}进行格式化；第二个f是对ype_of_people进行格式话
print(f"I also said: '{y}'")

hilarious = False
joke_evaluation = "Isn't that joke so funny?! {}"

print(joke_evaluation.format(hilarious))

w = "This is the left side of..."
e = "a string with a right side."

print(w + e)
#字符串之间可以进行加法

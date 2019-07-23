def loop(number):
    i = 0
    numbers = []

    while i < number:
        print(f"At the top i is {i}")
        numbers.append(i)


        i = i + 2
        print("Numbers now: ",numbers)
        print(f"At the bottom i is {i}")
    return numbers

print("The numbers: ")
total = int(input("请输入一个数："))
numbers = loop(total)
for num in numbers:
    print(num)

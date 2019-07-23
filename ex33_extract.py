
numbers = []
for i in range(0,6):  #厉害了，外界竟然影响不到
    print(f"At the top i is {i}")
    numbers.append(i)


    i = i + 2
    print("Numbers now: ",numbers)
    print(f"At the bottom i is {i}")

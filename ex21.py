def add(a, b):
    print(f"ADDING {a} + {b}")
    return a + b  #这个值不会在这里被打印出来

def substract(a, b):
    print(f"SUBSTRACT {a} - {b}")
    return a - b

def multiply(a, b):
    print(f"MULTIPY {a} * {b}")
    return a * b

def divide(a, b):
    print(f"DIVIEING {a} / {b}")
    return a / b


print("Let's do some math with just functions!")

age = add(30, 5)
height = substract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print(f"Age: {age}, Height: {height}, Weight: {weight}, IQ: {iq}")

print("Here is a puzzle.")

what = add(age, substract(height, multiply(weight, divide(iq, 2))))

print("That become: ", what, "Can you do it by hand?")

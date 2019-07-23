the_count = [1,2,3,4,5]
fruits = ['apples','orange','pears','apricots']
change = [1,'pennies',2,'dimes',3,'quarters']

for number in the_count:
    print(f"This is count {number}")

for fruit in fruits:
    print(f"A fruit of type:{fruit}")


for i in change:
    print(f"I got {i}")


elements = []

for elements in range(0,6):
    print(f"Adding {elements} to the list.")
    #elements.append(i)
print(elements)

for i in elements:
    print(f"Element was:{i}")

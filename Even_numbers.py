list = [
    2,
    3,
    4,
    7,
    1,
    10,
    8,
]

even_num = []
for even in list:
    if even % 2 == 0:
        even_num.append(even)
    else:
        pass
print("List of even numbers is: ", even_num)

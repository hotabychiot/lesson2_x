inOne = int(input("Введите число от 3 до 20  "))
print('') # Для отделения вывода результата
result = ""

i = 1
while i < inOne / 2:
    j = i + 1
    while j < inOne:
        if (inOne % (i + j)) == 0:
            result = result + str(i) + str(j)
        j += 1
    i += 1
print( result )
print('')  # Для отделения вывода результата


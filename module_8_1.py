def personal_sum(numbers):
    sum = 0
    incorrect_data = 0
    for num in numbers:
        try:
            sum += num
        except TypeError:
            print("Некорректный тип данных для подсчёта суммы -", num)
            incorrect_data +=1
    return (sum, incorrect_data)
def calculate_average(numbers):
 #   print(type(numbers), numbers)
    try:
        n =  personal_sum(numbers)[0]
        ss = 0
        for i in numbers:
            if isinstance(i, int):
                ss += 1
        n = n / ss

    except ZeroDivisionError:
        n = 0
    except TypeError:
        print("В numbers записан некорректный тип данных")
        n = None
    return n
if __name__ == '__main__':

    print(f'\033[4mРезультат 1:\033[0m \033[1m\033[32m{calculate_average("1, 2, 3")}\033[0m')  # Строка перебирается, но каждый символ - строковый тип
    print(f'\033[4mРезультат 2:\033[0m \033[1m\033[32m{calculate_average([1, "Строка", 3, "Ещё Строка"])}\033[0m')  # Учитываются только 1 и 3
    print(f'\033[4mРезультат 3:\033[0m \033[1m\033[32m{calculate_average(567)}\033[0m')  # Передана не коллекция
    print(f'\033[4mРезультат 4:\033[0m \033[1m\033[32m{calculate_average([42, 15, 36, 13])}\033[0m')  # Всё должно работать

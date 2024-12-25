class Car():
    def __init__(self, model, vin, number):
        self.model = model # - название автомобиля(строка)
        if self.__is_valid_vin(vin):
            self.__vin = vin #- vin номер автомобиля (целое число). Уровень доступа private.
        if self.__is_valid_numbers(number):
            self.__numbers = number #- номера автомобиля (строка).
    def  __is_valid_vin(self, vin_number):
        '''
        принимает vin_number и проверяет его на корректность.
        Возвращает True, если корректный, в других случаях выбрасывает исключение.
        VIN целое число, в диапазоне от 1000000 до 9999999 включительно
        Уровень доступа private.
        '''
        if type(vin_number) != int :
            raise IncorrectVinNumber('\033[31mНекорректный тип vin номер\033[0m')
            
        if vin_number < 1000000 or vin_number > 9999999:
            raise IncorrectVinNumber('\033[31mНеверный диапазон для vin номера\033[0m')
        return True
    def __is_valid_numbers(self, numbers):
        '''
         принимает numbers и проверяет его на корректность.
         Возвращает True, если корректный, в других случаях выбрасывает исключение.
         Строка должна состоять ровно из 6 символов.
         Уровень доступа private.
        '''
        if not isinstance(numbers, str):
            raise IncorrectCarNumbers('\033[31mНекорректный тип данных для номеров\033[0m')

        if len(numbers) != 6:
            raise  IncorrectCarNumbers('\033[31mНеверная длина номера\033[0m')
        return True

class  IncorrectVinNumber(Exception):
    def __init__(self, message):
        self.message = message

class IncorrectCarNumbers(Exception):
    def __init__(self, message):
        self.message = message




if __name__ == '__main__':
    try:
        first = Car('Model1', 1000000, 'f123dj') #
    except IncorrectVinNumber as exc:
        print(exc.message)
    except IncorrectCarNumbers as exc:
        print(exc.message)
    else:
        print(f'{first.model} успешно создан')

    try:
        second = Car('Model2', 300, 'т001тр')
    except IncorrectVinNumber as exc:
        print(exc.message)
    except IncorrectCarNumbers as exc:
        print(exc.message)
    else:
        print(f'{second.model} успешно создан')

    try:
        third = Car('Model3', 2020202, 'нет номера')
    except IncorrectVinNumber as exc:
        print(exc.message)
    except IncorrectCarNumbers as exc:
        print(exc.message)
    else:
        print(f'{third.model} успешно создан')

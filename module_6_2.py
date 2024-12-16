from math import sqrt

class Figure:
    sides_count = 5
    def __init__(self, colors):
        self.__sides = []
        self.__color = self.toList(colors)
        self.filled = True
# COLOR :
    @property
    def color(self):
        return self.__color
    @color.setter
    def color(self, color):
        color = self.toList(color)
        if len(color) == 3:
            self.__is_valid_color(color[0],color[1],color[2])
    def set_color(self, r, g, b):
        self.__is_valid_color(r,g,b)
    def __is_valid_color(self, r, g, b):
        if isinstance(r,int) and isinstance(g,int) and isinstance(b,int):
            if 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255:
                self.__color = [r,g,b]
# SIDE :
    def __is_valid_sides(self, param):
        b_param = False
        if len(param) == self.sides_count:
            b_param = True
            for i in param:
                if not (i >= 0 and isinstance(i,int)):
                    b_param = False
                    break
        return b_param

    @property
    def sides(self):
        return self.__sides

    @sides.setter
    def sides(self, new_sides):
        new_sides = self.toList(new_sides)
        if self.__is_valid_sides(new_sides):

            self.__sides = new_sides
        elif len(self.__sides) == 0:
            i = 0
            while i < self.sides_count:
                self.__sides.append(1)
                i +=1
    def __len__(self):
        sum = 0
        for i in self.sides:
            sum += i
        return sum

    def toList(self, param):
        if type(param) == int or type(param) == float:
            l1 = list({param})
        elif type(param) != list:
            l1 = list(param)
        else:
            l1 = param
        return l1

class Circle(Figure):
    def __init__(self, colors, side):
        super().__init__(colors)
        self.sides_count = 1
        self.sides = side
    def __radius(self):
        return 2 * 3.14159292 / self.sides[0]
    def get_square(self):
        return 3.14159292 * self.__radius() ** 2

class Triangle(Figure):
    def __init__(self, colors, side):
        super().__init__(colors)
        self.sides_count = 3
        self.sides = side
    def get_square(self):
        a = self.sides[0]
        b = self.sides[1]
        c = self.sides[2]
        p = (a + b + c) / 2
        return sqrt(p * (p - a) * (p - b) * (p - c))

class Cube(Figure):
    def __init__(self, colors, side):
        self.__sides = []
        super().__init__(colors)
        self.sides_count = 12
        self.sides = side
    def get_volume(self):
        return self.sides[0] ** 3

# SIDE :
    def __is_valid_sides(self, param):
        b_param = False
        if len(param) == self.sides_count:
            b_param = True
            valSide = param[0]
            for i in param:
                if not (i != valSide):
                    b_param = False
                    break
        elif len(param) == 1 and isinstance(param[0],int):
            b_param = True
        return b_param

    @property
    def sides(self):
        return self.__sides

    @sides.setter
    def sides(self, new_sides):
        new_sides = self.toList(new_sides)
        if self.__is_valid_sides(new_sides):
            if len(new_sides) == 1 and isinstance(new_sides[0], int):
                self.__sides = self.__genListSide(new_sides[0])
            else:
                 self.__sides = new_sides
        elif len(self.__sides) == 0:
            self.__sides = self.__genListSide(1)
    def __genListSide(self, val):
        i = 0
        listSide = []
        while i < self.sides_count:
            listSide.append(val)
            i += 1
        return listSide


if __name__ == '__main__':
    circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
    cube1 = Cube((222, 35, 130), 6)

    # Проверка на изменение цветов:

    circle1.color = (55, 66, 77)  # Изменится
    print(circle1.color)
    cube1.color = (300, 70, 15)  # Не изменится
    print(cube1.color)

    # Проверка на изменение сторон:
    cube1.sides = (5, 3, 12, 4, 5)  # Не изменится
    print(cube1.sides)
    circle1.sides = 15  # Изменится
    print(circle1.sides)

    # Проверка периметра (круга), это и есть длина:
    print(len(circle1))

    # Проверка объёма (куба):
    print(cube1.get_volume())





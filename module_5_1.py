class House:
    def __init__(self, name, levels):
        self.name = name
        self.levels = levels
    def __str__(self):
        return f"Название: {self.name}, кол-во этажей: {self.levels}"
    def __len__(self):
        return self.levels
    def __eq__(self, other):
        if isinstance(other, House):
            return self.levels == other.levels
        elif isinstance(other, int):
            return self.levels == other
        else:
            return False
    def __lt__(self, other):
        if isinstance(other, House):
            return self.levels < other.levels
        elif isinstance(other, int):
            return self.levels < other
        else:
            return False
    def __le__(self, other):
        if isinstance(other, House):
            return self.levels <= other.levels
        elif isinstance(other, int):
            return self.levels <= other
        else:
            return False
    def __gt__(self, other):
        if isinstance(other, House):
            return self.levels > other.levels
        elif isinstance(other, int):
            return self.levels > other
        else:
            return False
    def __ge__(self, other):
        if isinstance(other, House):
            return self.levels >= other.levels
        elif isinstance(other, int):
            return self.levels >= other
        else:
            return False
    def __ne__(self, other):
        if isinstance(other, House):
            return self.levels != other.levels
        elif isinstance(other, int):
            return self.levels != other
        else:
            return True
    def __add__(self, other):
        if isinstance(other, House):
            self.levels += other.levels
        else:
            self.levels += other
        return self
    def __radd__(self, other):
        self.levels += other
        return self
    def __iadd__(self, other):
        self.__add__(other)
        return self
# * * *
    def __sub__(self, other):
        if isinstance(other, House):
            self.levels -= other.levels
        else:
            self.levels -= other
        return self
    def __rsub__(self, other):
        self.levels = other - self.levels
        return self
    def __isub__(self, other):
        self.__sub__(other)
        return self
# * * *
    def __mul__(self, other):
        if isinstance(other, House):
            self.levels *= other.levels
        else:
            self.levels *= other
        return self
    def __rmul__(self, other):
        self.levels *= other
        return self
    def __imul__(self, other):
        self.__mul__(other)
        return self
# * * *
    def __truediv__(self, other):
        if isinstance(other, House):
            self.levels /= other.levels
        else:
            self.levels /= other
        return self
    def __rtruediv__(self, other):
        self.levels = other / self.levels
        return self
    def __itruediv__(self, other):
        self.__truediv__(other)
        return self
# P.S. Аналогичном способом можно переопределить и другие операторы ... :)

h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)
print('\n   *** Первый Этап ***   \n')
print(h1)
print(h2)
print(len(h1))
print(len(h2))
print('\n  *** Второй Этап *** \n')
print(h1)
print(h2)

print(h1 == h2)
h1 = h1 + 10
print(h1)
print(h1 == h2)
h1 += 10
print(h1)

h2 = 10 + h2
print(h2)

print(h1 > h2)
print(h1 >= h2)
print(h1 < h2)
print(h1 <= h2)
print(h1 != h2)


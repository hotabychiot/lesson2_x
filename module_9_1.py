
class StepValueError(ValueError):
    pass

class Iterator:
    def __init__(self, start, stop, step=1):
        if step == 0:
            raise StepValueError('шаг не может быть равен 0')
        self.start = start
        self.stop = stop
        self.step = step
        self.pointer = start
    def __iter__(self):
        self.pointer = self.start
        return self
    def __next__(self):
        if (self.pointer > self.stop and self.step > 0 ) or (self.pointer < self.stop and self.step < 0 ):
            raise StopIteration()
        old = self.pointer
        self.pointer += self.step
        return old


if __name__ == '__main__':
    try:
        iter1 = Iterator(100, 200, 0)
        for i in iter1:
            print(i, end=' ')
    except StepValueError:
        print('\033[31mШаг указан неверно\033[0m')
    iter2 = Iterator(-5, 1)
    iter3 = Iterator(6, 15, 2)
    iter4 = Iterator(5, 1, -1)
    iter5 = Iterator(10, 1)
    for i in iter2:
        print(i, end=' ')
    print()
    for i in iter3:
        print(i, end=' ')
    print()
    for i in iter4:
        print(i, end=' ')
    print()
    for i in iter5:
        print(i, end=' ')
    print()
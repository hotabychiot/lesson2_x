from  random import randint
class Animal:
    '''
    Класс описывающий животных.
    '''
    live = True
    sound = None # звук 
    _DEGREE_OF_DANGER = 0 # степень опасности существа
    def __init__(self, speed):
        self._cords = [0, 0, 0] # координаты в пространстве
        self.speed = speed # скорость передвижения существа

    def move(self, dx, dy, dz):
        self._cords[0] = dx * self.speed
        self._cords[1] = dy * self.speed
        dz *= self.speed
        if dz >= 0:
            self._cords[2] = dz
        else:
            print("It's too deep, i can't dive :(")
    def get_cords(self):
        print(f'X:{self._cords[0]}, Y:{self._cords[1]}, Z:{self._cords[2]}')
    def attack(self):
        if self._DEGREE_OF_DANGER < 5:
            print("Sorry, i'm peaceful :)")
        else:
            print("Be careful, i'm attacking you 0_0" )
    def speak(self):
        print(self.sound)

class Bird(Animal):
    '''
    Класс описывающий птиц.
    '''
    def __init__(self, speed):
        Animal.__init__(self,speed)
        self.beak = True

    def lay_eggs(self):
        print("Here are(is) ", int(randint(1, 4)), "eggs for you")
    def gg(self):
        print('gg1 : ', self.__class__, Bird.__mro__)

class AquaticAnimal(Animal):
    '''
    Класс описывающий плавающего животного
    '''
    def __init__(self):
        self._DEGREE_OF_DANGER = 3

    def dive_in(self, dz):
        self._cords[2] = abs(self._cords[2] - self.speed / 2 * dz)

class PoisonousAnimal(Animal):
    '''
    Класс описывающий ядовитых животных
    '''
    def __init__(self):
        self._DEGREE_OF_DANGER = 8


class Duckbill(Bird, AquaticAnimal, PoisonousAnimal):
    '''
    Класс описывающий утконоса
    '''
    def __init__(self, speed):
        Bird.__init__(self,speed)
        AquaticAnimal.__init__(self)
        PoisonousAnimal.__init__(self)
        self.sound = "Click-click-click"
    def gg(self):
        print('gg :', self.__class__, Duckbill.__mro__)


# *************

if __name__ == '__main__':

    db = Duckbill(10)
    print(db.live)
    print(db.beak)
    db.speak()
    db.attack()

    db.move(1, 2, 3)
    db.get_cords()
    db.dive_in(6)
    db.get_cords()
    db.lay_eggs()










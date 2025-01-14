import threading, random, queue
from time import sleep

class Table:
    def __init__(self, num):
        self.number = num
        self.guest = None

class Guest(threading.Thread):
    def __init__(self, name_g):
        self.name_g = name_g
        threading.Thread.__init__(self)
        self.daemon = True
    def run(self):
        sleep(random.randint(3, 10))

class Cafe:
    def __init__(self, *tables):
        self.queue = queue.Queue()
        self.tables = tables
    def guest_arrival(self, *guests):   # Прибытие гостей
        for g in guests:
            for t in self.tables:
                if t.guest is None:
                    print(f' {g.name_g} сел(-а) за стол номер {t.number}')
                    t.guest = g
                    t.guest.start()
                    break
            else:
                print(f'{g.name_g}  в очереди')
                self.queue.put(g)
    def discuss_guests(self):   #обслужить гостей
        quantity =len(self.tables) + 1
        while  (not self.queue.not_empty) or threading.active_count() > 1:
            if threading.active_count() < quantity:
                for t in self.tables:
                    if not t.guest is None:
                        if not t.guest.is_alive():
                            print(f"{t.guest.name_g} покушал(-а) и ушёл(ушла)")
                            print(f"Стол номер {t.number} свободен")
                            t.guest = None
                            if not self.queue.empty():
                                t.guest = self.queue.get()
                                print(f"{t.guest.name_g} вышел(-ла) из очереди и сел(-а) за стол номер {t.number}")
                                t.guest.start()
if __name__ == '__main__':
    # Создание столов
    tables = [Table(number) for number in range(1, 6)]
    # Имена гостей
    guests_names = ['Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman', 'Vitoria',
                    'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra' ]
    # Создание гостей
    guests = [Guest(name) for name in guests_names]
    # Заполнение кафе столами
    cafe = Cafe(*tables)
    # Приём гостей
    cafe.guest_arrival(*guests)
    # Обслуживание гостей
    cafe.discuss_guests()

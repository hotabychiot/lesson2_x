import threading, random
from time import sleep

class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()
    def deposit(self):
        for i in range(1, 100):
            payment = random.randint(50, 500)
            self.balance += payment
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            print(f'Пополнение: {payment}. Баланс: {self.balance}')
            sleep(0.001)


    def take(self):
        for i in range(1, 100):
            payment = random.randint(50, 500)
            print(f'Запрос на {payment}')
            if payment <= self.balance:
                self.balance -= payment
                print(f'Снятие: {payment}. Баланс: {self.balance}')
            else:
                print("Запрос отклонён, недостаточно средств")
                self.lock.acquire()
        pass


if __name__ == '__main__':
    bk = Bank()
    th1 = threading.Thread(target=Bank.deposit, args=(bk,))
    th2 = threading.Thread(target=Bank.take, args=(bk,))

    th1.start()
    th2.start()
    th1.join()
    th2.join()
    print(f'Итоговый баланс: {bk.balance}')
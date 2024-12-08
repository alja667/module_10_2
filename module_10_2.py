import threading
import time

class  Knight(threading.Thread):

    def __init__(self, name, power):
        threading.Thread.__init__(self)
        self.name = str(name)
        self.power = int(power)
        self.counter = 100

    def run (self):
        print(f'{self.name}, на нас напали!')
        day = 0
        while self.counter >0 and self.counter !=0  :
            time.sleep(1)
            day +=1
            self.counter -=self.power
            print(f'{self.name} сражается {day}..., осталось {self.counter} воинов.')
        print(f'{self.name} одержал победу спустя {day} дней(дня)!')
        




first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)
first_knight.start()
second_knight.start()




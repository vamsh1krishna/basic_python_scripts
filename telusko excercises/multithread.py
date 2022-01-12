from threading import *
from time import sleep

class Hello(Thread):
    def run(self):
        for i in range(50):
            print('hello')
            sleep(0.4)


class Hi(Thread):
    def run(self):
        for i in range(50):
            print('hi')
            sleep(0.4)

t1= Hello()
t2= Hi()

t1.start()
sleep(0.2)
t2.start()

t1.join()
t2.join()

print('Bye')
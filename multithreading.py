import threading
import time


def breakfast():
    time.sleep(3)
    print("you eat breakfast")

def drink_coffee():
    time.sleep(4)
    print("you drink coffee")

def studying():
    time.sleep(5)
    print("you study")


x = threading.Thread(target=breakfast, args=())
x.start()

y = threading.Thread(target=drink_coffee, args=())
y.start()

z = threading.Thread(target=studying, args=())
z.start()

# breakfast()
# drink_coffee()
# studying()
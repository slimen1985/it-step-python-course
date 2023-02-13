import time
import threading


def remind():
    reminder = input("О чем вам напомнить? ")
    duration = int(input("Через сколько секунд? "))
    time.sleep(duration)
    print(reminder)


thread = threading.Thread(target=remind)
thread.start()

print("Пока поток работает, мы можем сделать что нибудь еще.")

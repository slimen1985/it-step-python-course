import time
import os
import threading


def find_wow(file_name):
    while True:
        if os.path.exists(file_name):
            with open(file_name, 'r') as file:
                if 'Wow!' in file.read():
                    file.close()
                    event.set()
                    break
                else:
                    file.close()
                    time.sleep(5)
        else:
            time.sleep(5)


def delete_file(event):
    event.wait()
    os.remove('file.txt')


def create_file():
    with open('file.txt', 'w') as file:
        file.write('This is a file with some text. Wow!')
        file.close()


# Создаем файл
create_file()

# Создаем объект события
event = threading.Event()

# Создаем потоки для функций
t1 = threading.Thread(target=find_wow, args=('file.txt',))
t2 = threading.Thread(target=delete_file, args=(event,))

# Запускаем потоки
t1.start()
t2.start()

# Ожидаем завершения потоков
t1.join()
t2.join()

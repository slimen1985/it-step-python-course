import socket

UPD_IP = "127.0.0.1"
UPD_PORT = 8001

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UPD_IP, UPD_PORT))

print("UPD-сервер запущен!")

while True:
    data, addr = sock.recvfrom(1024)
    message = data.decode()
    if message.startswith("new_device"):
        device_id = message.split()[1]
        print(f"Новое устройство подключено: {device_id}")




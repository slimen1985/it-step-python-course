import socket
import uuid

UDP_IP = "127.0.0.1"
UDP_PORT = 8001

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

device_id = str(uuid.uuid4())  # генерация уникального идентификатора устройства
message = f"new_device {device_id}"
sock.sendto(message.encode(), (UDP_IP, UDP_PORT))

print("UDP клиент отправил сообщение")

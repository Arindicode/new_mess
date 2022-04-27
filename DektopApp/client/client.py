import socket
from threading import Thread

#Новый сокет
client_socket = socket.socket()

#Подключение к серверному сокету
client_socket.connect(("127.0.0.1", 5000))

#Создаём ф-и отправки и получения сообщений
def sender():
    while True:
        a = input() #Читаем строку с клавиатуры
        client_socket.send(a.encode("utf-8")) #Отправляем её, предварительно закодировав
def reciver():
    while True:
        b = client_socket.recv(1024) #Получаем строку от сервера
        print(b.decode("utf-8")) #Печатаем, предварительно раскодировав

#Создаём по отдельному потоку для каждой функции
tread1 = Thread(target=sender)
tread2 = Thread(target=reciver)

#Потоки запушены, клиент готов получать и отправлять сообщения
tread1.start()
tread2.start()
import socket
from threading import Thread #Подключение класса потока

new_socket = socket.socket() #Создание объекта сокет
new_socket.bind(('127.0.0.1', 5000)) #Привязка объекта к ip и порту
new_socket.listen(2) #Сокет общается с двумя другими

print("Сервер поднят и готов к работе")

conn1, add1 = new_socket.accept() #Сохранение объекта сокета клиента и его адрес
print("Привет, ты подключился! Ждем второго.")

conn2, add2 = new_socket.accept() #Сохранение объекта сокета клиента и его адрес
print("И второй подключился! Общайтесь.")

# Запуск бесконечного цикла
def acceptor1():
    while True:
        a = conn1.recv(1024) #Получение инфорации от первого юзера
        conn2.send(a) #Передача инфы второму юзеру

def acceptor2():
    while True:
        b = conn2.recv(1024) #Получение инфорации от второго юзера
        conn1.send(b) #Передача инфы первому юзеру

#Потоки
tread1 = Thread(target=acceptor1)
tread2 = Thread(target=acceptor2)

#Запуск потоков
tread1.start()
tread2.start()
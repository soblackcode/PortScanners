# -*- coding: utf-8 -*-
 
 
import socket # импорт библиотеки socket
 
 
def main(): # Главная функция
    host = input('[*] Enter Host: ') # ввод сайта для сканирования
    port = int(input('[*] Enter Port: ')) # ввод порта для сканирования
 
    try: # пробуем сделать следующе е...
        s = socket.socket() # создания сокета
        s.settimeout(0.5) # задаём таймаут для подключения
        scan = s.connect((host, port)) # пробуем подключится к данным, которые ввёл пользователь
        print('[+] Host: ' + host + ' Port: ' + str(port) + ' - OPENED') # Если всё прошло без ошибкок, то выводим, что порт открыт
    except socket.error: # если при выполнение произошла socket ошибка, то...
        print('[-] Host: ' + host + ' Port: ' + str(port) + ' - CLOSED') # Выводим, что порт закрыт
 
 
main() # Вызов главной функции

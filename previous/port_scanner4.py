# -*- coding: utf-8 -*-


import socket # импорт библиотеки socket
import threading # импорт библиотеки для многопоточности
from colorama import Fore, Style, init # импорт модулей Fore, Init и Style из библиотеки colorama
from os import name, system # импорт модуля name для определения системы, импорт system для выполнения системных команд


if name == 'nt': # Если у пользователя windows, то...
	init() # Выполнение функции init из библиотеки colorama


def clear(): # создание функции очитски экрана
	if name == 'nt': # Если у пользователя windows, то...
		system('cls') # Выполнение системной команды 'cls' для очистки экрана
	else: # В противном случае...
		system('clear') # Выполнение системной команды 'clear' для очистки экрана 


# Слоаврь с портами и их обозначениями
ports = {
    20: 'FTP-DATA', 21: 'FTP', 22: 'SSH', 23: 'Telnet', 25: 'SMTP', 42: 'NAMESERVER',
    43: 'WHOIS', 53: 'DOMAIN (DNS)', 67: 'BOOTPS', 69: 'TFTP', 80: 'HTTP', 110: 'POP3', 139: 'NETBIOS-SSN', 443: 'TCP - HTTPS',
    1080: 'SOCKS', 3128: 'HTTP used by Web caches', 3389: 'RAdmin', 5900: 'Virtual Network Computing (VNC)',
    8000: 'iRDMI', 8008: 'HTTP_ALT', 8080: 'WEBCACHE', 8888: 'NewsEDGE server'}

def single_scanning(host, port): # функцию сканирования одного порта
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # создание сокета
	s.settimeout(0.5) # Ставим таймаут для сканирования
	try: # пробуем сделать следующее
		connection = s.connect((host, port)) # пробуем подключиться к порту
	except socket.error: # если ошибка, то...
		print(Fore.RED + '[-] Port: ' + str(port) + ' - CLOSED') # вывод о том, что порт закрыт (красный цвет)
	else: # если ошибки не было, то...
		try: # пробем получить ключ из словаря
			print(Fore.GREEN + '[+] Port: ' + str(port) + '(' + ports[port] + ')' + ' - OPEN') # пробуем вытянуть порт из словаря(такого порта может не быть в словаре) (зеленый цвет)
		except: # если ошибка, то...
			print(Fore.GREEN + '[+] Port: ' + str(port) + ' - OPEN') # Выводим, что порт открыт, не берём значение из словаря (зеленый цвет)


def all_scanning(host, port): # сканирование всех портов в словаре
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # создание сокета
	s.settimeout(0.5) # Ставим таймаут для сканирования
	try: # пробуем сделать следующее...
		connection = s.connect((host, port)) # пробуем подключиться к порту
		print(Fore.GREEN + '[+] ' + ' Port: ' + str(port) + '(' + ports[port] + ') - OPEN') # если все прошло успешно, то вывод о том, что порт открыт (зеленый цвет)
	except socket.error: # если ошибка socket'а, то...
		pass # заглушка(ничего не делаем)

def main(): # главная функция
	clear() # Вызов функции очистки экрана
	print(Fore.GREEN + '''
		|-------------------|
		|    PortScanner    |
		|                   |
		|                   |
		|    BLACK  CODE    |
		|-------------------|
		''') # Вывод зеленым цветом приветсвенное сообщение
	print(Fore.YELLOW + '''
		1 - Single Port Scanning
		2 - All Ports Scanning
		''') # Вывод желтым цветом о выборе режима
	mode = input(Fore.YELLOW + '\n[*] Enter Mode (1/2): ') # пользователь выбирает режим(желтый цвет)
	clear() # Вызов функции очистки экрана
	if mode == '1': # если пользователь ввёл 1, то...
		host = input(Fore.YELLOW + '[*] Enter Host: ') # запрос цели у пользователя(желтый цвет)
		port = int(input(Fore.YELLOW + '\n[*] Enter Port: ')) # запрос порта у пользователя(желтый цвет)
		print(Fore.YELLOW + '\n[*] Scanning...\n') # (желтый цвет)
		single_scanning(host, port) # запуск функции сканирования одного порта
	elif mode == '2': # если пользователь ввёл 2, то...
		host = input(Fore.YELLOW + '[*] Enter Host: ') # запрос цели у пользователя(жетый цввет)
		print(Fore.YELLOW + '\n[*] Scanning...') # (желтый цвет)
		print(Fore.GREEN + '\n[*] Open Ports:\n') # (зеленый цвет)
		for port in ports: # перебор всех портов из словаря 
			thread = threading.Thread(target=all_scanning, kwargs={'host': host, 'port': port}) # создание потока, цель которого - функция "all_scanning", с аргументами - host, port
			thread.start() # запускем поток
		thread.join() # подсоединени потока к основному(чтобы программа дальше работала)
	else: # если пользователь ввёл что-то другое, то...
		print(Fore.RED + '[!] ERROR: Wrong Mode!') # Вывод сообщения о ошибке (красный цвет)
		print(Style.RESET_ALL) # Сброс цветов
		exit(1) # Выход из программы
	print(Style.RESET_ALL) # Сброс цветов


main() # Вызов главной функции
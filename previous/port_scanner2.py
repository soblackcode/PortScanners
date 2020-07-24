# -*- coding: utf-8 -*-


import socket # импорт библиотеки socket


# Слоаврь с портами и их обозначениями
ports = {
    20: 'FTP-DATA', 21: 'FTP', 22: 'SSH', 23: 'Telnet', 25: 'SMTP', 42: 'NAMESERVER',
    43: 'WHOIS', 53: 'DOMAIN (DNS)', 67: 'BOOTPS', 69: 'TFTP', 80: 'HTTP', 110: 'POP3', 139: 'NETBIOS-SSN',
    1080: 'SOCKS', 3128: 'HTTP used by Web caches', 3389: 'RAdmin', 5900: 'Virtual Network Computing (VNC)',
    8000: 'iRDMI', 8008: 'HTTP_ALT', 8080: 'WEBCACHE', 8888: 'NewsEDGE server'}


def single_scanning(host, port): # функцию сканирования одного порта
	print('[*] Scanning...')

	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # создание сокета
	s.settimeout(0.5) # Ставим таймаут для сканирования
	try: # пробуем сделать следующее
		connection = s.connect((host, port)) # пробем подключиться к порту
	except socket.error: # если ошибка, то...
		print('[-] Port: ' + str(port) + ' - CLOSED') # вывод о том, что порт закрыт
	else: # если ошибки не было, то...
		try: # пробем получить ключ из словаря
			print('[+] Port: ' + str(port) + '(' + ports[port] + ')' + ' - OPENED') # пробуем вытянуть порт из словаря(такого порта может не быть в словаре)
		except: # если ошибка, то...
			print('[+] Port: ' + str(port) + ' - OPENED') # Выводим, что порт открыт, не берём значение из словаря


def all_scanning(host): # сканирование всех портов в словаре
	print('[*] Scanning...')


	for port in ports: # перебор всех портов из словаря "ports"
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # создание сокета
		s.settimeout(0.5) # Задаём таймаут для сканирования
		try:
			connection = s.connect((host, port)) # пробуем подключиться к одному из портов
		except socket.error: # если ошибка, то просто пропускаем и ничего не выводим
			pass 
		else: # если ошибки не было, то...
			print('[+] Port: ' + str(port) + '(' + ports[port] + ') - OPENED') # сообщаем о том, что порт открыт


def main(): # главная функция
	print('''
		1 - Single Port Scanning
		2 - All Ports Scanning
		''') # Вывод о выборе режима
	mode = input('[*] Enter Mode (1/2): ') # пользователю выбирает режим

	if mode == '1': # если пользователь ввёл 1, то...
		host = input('[*] Enter Host: ') # запрос цели у пользователя
		port = int(input('[*] Enter Port: ')) # запрос порта у пользователя
		single_scanning(host, port) # запуск функции сканирования одного порта
	elif mode == '2': # если пользователь ввёл 2, то...
		host = input('[*] Enter Host: ') # запрос цели у пользователя
		all_scanning(host) # запуск функции сканирования всех портов
	else: # если пользователь ввёл что-то другое, то...
		print('[!] ERROR: Wrong Mode!')
		exit(1) # выход из программы


main() # Вызов главной функции


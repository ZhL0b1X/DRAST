import re
import time 
import cursor
import inquirer
import os, sys
import animation
import dns.resolver
import pyfiglet as pf
from datetime import datetime
from termcolor import colored
from lib.resolvetype import Makefile




if __name__ == "__main__":
	while True:
		os.system('cls' if os.name == 'nt' else 'clear')
		logo_text     = pf.figlet_format("DNS resolver", font='slant')
		logo          = colored(logo_text, 'blue')
		print(logo)
		symbol_red    = colored("[!]", "red")
		processing 	  = colored("Processing", "green")
		symbol_yellow = colored("[!]", "yellow")
		pattern       = re.compile('^([A-Za-z0-9]\.|[A-Za-z0-9][A-Za-z0-9-]{0,61}[A-Za-z0-9]\.){1,3}[A-Za-z]{2,6}$')
		main_menu     = [inquirer.List("main", message="Choose option", choices=["Single domain resolve", "Bulk resolve", "Add to db", "Exit"])]
		format_menu   = [inquirer.List("format", message="Choose format", choices=["Json" , "Dictionary"])]
		suspended_db  = [inquirer.List("format", message="Would you like to turn on suspended mode?", choices=["Yes" , "No"])]
		wait          = animation.Wait(color="green", speed=0.1)
		file          = Makefile()
		cursor.hide()
		main_answer   = inquirer.prompt(main_menu)
		os.system('cls' if os.name == 'nt' else 'clear')
		if str(main_answer) == "{'main': 'Exit'}":
			sys.exit()
		os.system('cls' if os.name == 'nt' else 'clear')
		cursor.show()
		os.system('cls' if os.name == 'nt' else 'clear')
		while True:
			try:
				dns_ip    = dns.resolver.Resolver()
				input_dns = [input('Enter DNS IP or press "Enter" to use the default IP: ')]
				os.system('cls' if os.name == 'nt' else 'clear')
				if input_dns == [""]:
					dns_ip
				else:
					dns_ip.nameservers = input_dns
			except ValueError:
					print("\n\n\n" + symbol_red + " Invalid DNS ip " + symbol_red + "\n" +
					symbol_red + "Please try again" + symbol_red)
					time.sleep(2)
					os.system('cls' if os.name == 'nt' else 'clear')
					continue
			break
		if str(main_answer) == "{'main': 'Add to db'}":
			cursor.hide()
			suspended_ansewer = inquirer.prompt(suspended_db)
			if str(suspended_ansewer) == "{'format': 'Yes'}":
				os.system('cls' if os.name == 'nt' else 'clear')
				print(processing)
				file.database(dns_ip, suspended_mode=True)
			elif str(suspended_ansewer) == "{'format': 'No'}":
				os.system('cls' if os.name == 'nt' else 'clear')
				wait.start()
				file.database(dns_ip, suspended_mode=False)
		if str(main_answer) == "{'main': 'Single domain resolve'}":
			format_answer = inquirer.prompt(format_menu)
			while True:
				os.system('cls' if os.name == 'nt' else 'clear')
				print("Please write domain in next format: \n\n1: example.com \n\n2: www.example.com\n")
				domain = input("Please type domain: ")
				match  = re.search(pattern, domain)
				if match:
					break
				else:
					print("\n\n\n" + symbol_red + " Domain is not valid. Please try again! " + symbol_red)
					time.sleep(2)
					os.system('cls' if os.name == 'nt' else 'clear')
					continue
			os.system('cls' if os.name == 'nt' else 'clear')
			cursor.hide()
			wait.start()
			if str(format_answer) == "{'format': 'Json'}":
				file.single(domain, dns_ip, json=True)
			elif str(format_answer) == "{'format': 'Dictionary'}":
				file.single(domain, dns_ip, json=False) 
		elif str(main_answer) == "{'main': 'Bulk resolve'}":
			format_answer = inquirer.prompt(format_menu)
			cursor.hide()
			print(symbol_yellow + " Be sure that you edit domain_list.txt " + symbol_yellow)
			wait.start()
			if str(format_answer) == "{'format': 'Json'}":
				file.bulk(dns_ip, json=True)
			elif str(format_answer) == "{'format': 'Dictionary'}":
				file.bulk(dns_ip, json=False)
		os.system('cls' if os.name == 'nt' else 'clear')
		wait.stop()
		print("Data saved")
		time.sleep(1.5)
		os.system('cls' if os.name == 'nt' else 'clear')    




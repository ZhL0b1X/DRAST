import re
import time 
import cursor
import os, sys
import inquirer
import argparse
import animation
import dns.resolver
import pyfiglet as pf
from datetime import datetime
from termcolor import colored
from lib.resolvetype import Makefile


def interactive_mode():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        logo_text     = pf.figlet_format("DRAST", font='slant')
        defenition    = colored("DNS Record Analysis and Storage Tool", 'blue')
        logo          = colored(logo_text, 'blue')
        print(logo)
        print(defenition + "\n")
        symbol_red    = colored("[!]", "red")
        processing    = colored("Processing", "green")
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

def main():
    Make = Makefile()
    drast_description = (
        "DRAST: A DNS record analysis and collection tool.\n"
        "Gathers A, AAAA, MX, NS, SOA, TXT, CNAME records.\n"
        "Stores data in JSON, dictionary, or SQLite3 formats.\n"
        "Supports customization with a changeable DNS IP address.\n"
        "Provides A record location information.\n"
        "Features basic command execution and interactive CLI modes.\n"
        "Includes suspended mode for real-time edits to dns_domains.txt during continuous operation."
    )
    parser = argparse.ArgumentParser(
        description=drast_description
        ) 
    mode_group = parser.add_mutually_exclusive_group(required=True)
    mode_group.add_argument("-I", "--interactive", action="store_true", help="Enable interactive mode for a user-friendly command-line interface.")
    mode_group.add_argument("--sql", action="store_true", help="Enable SQL-related functionality")
    mode_group.add_argument("-s", "--single", metavar="example.com", help="Resolve a single domain.")
    mode_group.add_argument("-b", "--bulk", action="store_true", help="Bulk resolve domains from a file.")
    output_format_group = parser.add_mutually_exclusive_group()
    output_format_group.add_argument("-j", "--json", action="store_true", help="Create a JSON file.")
    output_format_group.add_argument("-d", "--dictionary", action="store_true", help="Create a dictionary file.")
    parser.add_argument("-i", "--input_file", nargs='?', metavar="/path/to/file/txt", help="Optional flag to specify the path to a file containing a list of domains. Only applicable with --sql or -b/--bulk.")
    parser.add_argument("--dns", metavar="[IP]", help="Specify DNS IP address.")
    parser.add_argument("-o", "--output_directory", metavar="/output/path", help="Specify the output path for both -s and -b")
    parser.add_argument("-S", "--suspended", action="store_true", help="Enable suspended mode for SQL")

    args = parser.parse_args()

    dns_ip = dns.resolver.Resolver()
            
    if args.dns:
        dns_ip.nameservers = [args.dns]
    else:   
        dns_ip 

    if args.interactive:
        if any([args.single, args.output_directory, args.sql, args.bulk, args.suspended,  args.json, args.input_file, args.dictionary, args.dns]):
            print("Error: Interactive mode cannot be used with other flags.")
        else:
            interactive_mode()
    elif args.sql:
        input_file = args.input_file if args.input_file else None
        if any([args.single, args.bulk,  args.json, args.dictionary, args.output_directory]):
            print("Error: SQL mode cannot be used with other flags except: --suspended, --input_file,  --dns.")
        else:
            if args.input_file:
                if args.suspended:
                    Make.database(dns_ip, input_file, suspended_mode=True)
                else:
                    Make.database(dns_ip, input_file, suspended_mode=False)
            else:
                if args.suspended:
                    Make.database(dns_ip, input_file, suspended_mode=True)
                else:
                    Make.database(dns_ip, input_file, suspended_mode=False)
    elif args.suspended:
        symbol_red = colored("Error: ", "red")
        print("\n" + symbol_red + "To use --suspended/-S you need specify --sql first\n")
        parser.print_help()
        exit(1)
    elif args.single:
        if any([args.sql, args.bulk, args.suspended, args.input_file]):
            print("Error: single mode cannot be used with: --sql --bulk --input_file --suspended --interactive.")
        else:
            output_directory = args.output_directory if args.output_directory else None
            if args.output_directory:
                if args.json:
                    Make.single(args.single, dns_ip, output_directory,  json=True)
                elif args.dictionary:
                    Make.single(args.single, dns_ip, output_directory, json=False)
                else:
                    Make.single(args.single, dns_ip, output_directory, json=True)
            else:
                if args.json:
                    Make.single(args.single, dns_ip, output_directory, json=True)
                elif args.dictionary:
                    Make.single(args.single, dns_ip, output_directory, json=False)
                else:
                    Make.single(args.single, dns_ip, output_directory, json=True)
    elif args.bulk:
        input_file = args.input_file if args.input_file else None
        output_directory = args.output_directory if args.output_directory else None
        if args.output_directory:        
            if args.input_file:
                if args.json:
                    Make.bulk(dns_ip, input_file, output_directory, json=True)
                elif args.dictionary:
                    Make.bulk(dns_ip, input_file, output_directory, json=False)
                else:
                    Make.bulk(dns_ip, input_file, output_directory, json=True)
            elif args.json:
                Make.bulk(dns_ip, input_file, output_directory, json=True)
            elif args.dictionary:
                Make.bulk(dns_ip, input_file, output_directory, json=False)
            else:
                Make.bulk(dns_ip, input_file, output_directory, json=True)
        else:
            if args.input_file:
                if args.json:
                    Make.bulk(dns_ip, input_file, output_directory, json=True)
                elif args.dictionary:
                    Make.bulk(dns_ip, input_file, output_directory, json=False)
                else:
                    Make.bulk(dns_ip, input_file, output_directory, json=True)
            elif args.json:
                Make.bulk(dns_ip, input_file, output_directory, json=True)
            elif args.dictionary:
                Make.bulk(dns_ip, input_file, output_directory, json=False)
            else:
                Make.bulk(dns_ip, input_file, output_directory, json=True)
    elif args.input_file:
        symbol_red = colored("Error: ", "red")
        print("\n" + symbol_red + "To use --input_file/-i you need specify -b/--bulk or --sql first.\n")
        parser.print_help()
        exit(1)
    elif args.output_directory:
        symbol_red = colored("Error: ", "red")
        print("\n" + symbol_red + "To use --output_directory/-o you need specify --single or --bulk mode first\n")
        parser.print_help()
        exit(1)
    else:
        print("Invalid combination of options. Please specify --single, --bulk, --sql, or --interactive.")
    

if __name__ == "__main__":
    main()



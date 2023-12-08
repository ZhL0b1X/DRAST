#!/usr/bin/env python3

import json
import time
import os
import sqlite3
from datetime import datetime
from lib.dnsresolver import DomainInfo
import signal


def handle_interrupt(signum, frame):
    print("\nExiting gracefully...")
    exit(0)

signal.signal(signal.SIGINT, handle_interrupt)


class Makefile:

    def __init__(self):
        self.date = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        self.file = os.path.join("Domain_list", "dns_domains.txt")

    def write_to_file(self, domain_object, file):
        record_types = ['A', 'AAAA', 'MX', 'TXT', 'CNAME', 'NS', 'SOA', 'PTR', 'SRV', 'CAA']
        file.write('\n'.join([json.dumps(domain_object.resolve(record_type, json_format=True)) for record_type in record_types]) + '\n')

    def process_domain(self, url, dns, json_format):
        domain_object = DomainInfo(url, dns)
        output_directory = "Output"
        os.makedirs(output_directory, exist_ok=True)
        with open(os.path.join(output_directory, self.date + ".txt"), "a") as file:
            self.write_to_file(domain_object, file)

    def single(self, url, dns, output_directory=None, json=True):
        self.process_domain(url, dns, json)

    def bulk(self, dns, input_file=None, output_directory=None, json=True):
        if not os.path.exists(input_file):
            print(f"Error: File not found at '{input_file}'. Please check the file path and try again.")
            return
        
        input_file = input_file or self.file
        with open(input_file, 'r') as file:
            for url in file:
                self.process_domain(url.strip(), dns, json)

    def database(self, dns, input_file=None, suspended_mode=False):
        conn = sqlite3.connect('resolver.db')
        conn.execute('''CREATE TABLE IF NOT EXISTS dns_records
                         (date_time TEXT, domain_name TEXT, record_type TEXT,
                          resolver TEXT, status TEXT, data TEXT)''')
        input_file = input_file or self.file
        while True:
            with open(input_file, 'r') as file:
                for url in file:
                    domain_object = DomainInfo(url.strip(), dns)
                    for record_type in ['A', 'AAAA', 'MX', 'TXT', 'CNAME', 'NS', 'SOA', 'PTR', 'SRV', 'CAA']:
                        data = json.dumps(domain_object.resolve(record_type, json_format=False)['data'])
                        conn.execute('''INSERT INTO dns_records
                                         (date_time, domain_name, record_type, resolver, status, data)
                                         VALUES (?, ?, ?, ?, ?, ?)''',
                                     (domain_object.time, url, record_type, domain_object.resolver, 'OK', data))
            conn.commit()
            if not suspended_mode:
                break
            time.sleep(10)
        conn.close()

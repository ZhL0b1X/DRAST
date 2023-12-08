#!/usr/bin/env python3

import time 
import json
import sqlite3
import os, sys
from datetime import datetime
from lib.dnsresolver import Domaininfo
import signal


def handle_interrupt(signum, frame):
    print("\nExiting gracefully...")
    exit(0)

signal.signal(signal.SIGINT, handle_interrupt)

class Makefile(object):

    def __init__(self):
        super(Makefile, self).__init__()
        self.date = datetime.now().strftime('D%Y-%m-%dT%H-%M-%S')
        self.file = os.path.join("Domain_list", "dns_domains.txt")


    def single(self, url, dns, output_directory=None, json=True):
        domain_object  = Domaininfo(url, dns)
        if json == False:
            resolveA = domain_object.resolveA(json_format=False)
            resolveAAAA = domain_object.resolveAAAA(json_format=False)
            resolveMX = domain_object.resolveMX(json_format=False)
            resolveTXT = domain_object.resolveTXT(json_format=False)
            resolveCNAME = domain_object.resolveCNAME(json_format=False)
            resolveNS = domain_object.resolveNS(json_format=False)
            resolveSOA = domain_object.resolveSOA(json_format=False)
            resolvePTR = domain_object.resolvePTR(json_format=False)
            resolveSRV = domain_object.resolveSRV(json_format=False)
            resolveCAA = domain_object.resolveCAA(json_format=False)
        else:
            resolveA = domain_object.resolveA(json_format=True)
            resolveAAAA = domain_object.resolveAAAA(json_format=True)
            resolveMX = domain_object.resolveMX(json_format=True)
            resolveTXT = domain_object.resolveTXT(json_format=True)
            resolveCNAME = domain_object.resolveCNAME(json_format=True)
            resolveNS = domain_object.resolveNS(json_format=True)
            resolveSOA = domain_object.resolveSOA(json_format=True)
            resolvePTR = domain_object.resolvePTR(json_format=True)
            resolveSRV = domain_object.resolveSRV(json_format=True)
            resolveCAA = domain_object.resolveCAA(json_format=True)
        if output_directory is None:
            os.makedirs("Output", exist_ok=True)
            file = open(os.path.join("Output", self.date + ".txt"), "a")
        else:
            file = open(os.path.join(output_directory, self.date + ".txt"), "a")
        file.write("%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n" % (
                                                    str(resolveA), 
                                                    str(resolveAAAA),
                                                    str(resolveMX), 
                                                    str(resolveTXT), 
                                                    str(resolveCNAME), 
                                                    str(resolveNS), 
                                                    str(resolveSOA),
                                                    str(resolvePTR), 
                                                    str(resolveSRV), 
                                                    str(resolveCAA))
                                                    )
        file.close()


    def bulk(self, dns, input_file=None, output_directory=None, json=True):
        if input_file is None:
            input_file = self.file
        with open(input_file, 'r') as file:
            file_content = file.readlines()
        for url in file_content:
            url = url.strip()   
            domain_object = Domaininfo(url, dns)
            if json == False:
                resolveA = domain_object.resolveA(json_format=False)
                resolveAAAA = domain_object.resolveAAAA(json_format=False)
                resolveMX = domain_object.resolveMX(json_format=False)
                resolveTXT = domain_object.resolveTXT(json_format=False)
                resolveCNAME = domain_object.resolveCNAME(json_format=False)
                resolveNS = domain_object.resolveNS(json_format=False)
                resolveSOA = domain_object.resolveSOA(json_format=False)
                resolvePTR = domain_object.resolvePTR(json_format=False)
                resolveSRV = domain_object.resolveSRV(json_format=False)
                resolveCAA = domain_object.resolveCAA(json_format=False)
            else:
                resolveA = domain_object.resolveA(json_format=True)
                resolveAAAA = domain_object.resolveAAAA(json_format=True)
                resolveMX = domain_object.resolveMX(json_format=True)
                resolveTXT = domain_object.resolveTXT(json_format=True)
                resolveCNAME = domain_object.resolveCNAME(json_format=True)
                resolveNS = domain_object.resolveNS(json_format=True)
                resolveSOA = domain_object.resolveSOA(json_format=True)
                resolvePTR = domain_object.resolvePTR(json_format=True)
                resolveSRV = domain_object.resolveSRV(json_format=True)
                resolveCAA = domain_object.resolveCAA(json_format=True)
            if output_directory is None:
                os.makedirs("Output", exist_ok=True)
                file = open(os.path.join("Output", self.date + ".txt"), "a")
            else:
                file = open(os.path.join(output_directory, self.date + ".txt"), "a")
            file.write("%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n" % (
                                                        str(resolveA), 
                                                        str(resolveAAAA),
                                                        str(resolveMX), 
                                                        str(resolveTXT), 
                                                        str(resolveCNAME), 
                                                        str(resolveNS), 
                                                        str(resolveSOA),
                                                        str(resolvePTR), 
                                                        str(resolveSRV), 
                                                        str(resolveCAA))
                                                        )
            file.close()


    def database(self, dns, input_file=None, suspended_mode=False):
        conn = sqlite3.connect('resolver.db')

        conn.execute('''CREATE TABLE IF NOT EXISTS dns_records
                         (date_time TEXT, domain_name TEXT, record_type TEXT,
                          resolver TEXT, status TEXT, data TEXT)''')
        try:    
            while True:
                if input_file is None:
                    input_file = self.file
                with open(input_file, 'r') as file:
                    file_content = file.readlines()
                for url in file_content:
                    url = url.strip()
                    domain_object  = Domaininfo(url, dns)
                    resolveA = domain_object.resolveA(json_format=False)
                    resolveAAAA = domain_object.resolveAAAA(json_format=False)
                    resolveMX = domain_object.resolveMX(json_format=False)
                    resolveTXT = domain_object.resolveTXT(json_format=False)
                    resolveCNAME = domain_object.resolveCNAME(json_format=False)
                    resolveNS = domain_object.resolveNS(json_format=False)
                    resolveSOA = domain_object.resolveSOA(json_format=False)
                    resolvePTR = domain_object.resolvePTR(json_format=False)
                    resolveSRV = domain_object.resolveSRV(json_format=False)
                    resolveCAA = domain_object.resolveCAA(json_format=False)

                    for result in resolveA['data']:
                        data_json = json.dumps(result)
                        conn.execute('''INSERT INTO dns_records
                                         (date_time, domain_name, record_type, resolver, status, data)
                                         VALUES (?, ?, ?, ?, ?, ?)''',
                                     (resolveA['date_time'], resolveA['domain_name'], resolveA['record_type'], resolveA['resolver'], resolveA['status'], data_json))

                    conn.execute('''INSERT INTO dns_records
                                     (date_time, domain_name, record_type, resolver, status, data)
                                     VALUES (?, ?, ?, ?, ?, ?)''',
                                 (resolveAAAA['date_time'], resolveAAAA['domain_name'], resolveAAAA['record_type'], resolveAAAA['resolver'], resolveAAAA['status'], resolveAAAA['data']))

                    conn.execute('''INSERT INTO dns_records
                                     (date_time, domain_name, record_type, resolver, status, data)
                                     VALUES (?, ?, ?, ?, ?, ?)''',
                                 (resolveMX['date_time'], resolveMX['domain_name'], resolveMX['record_type'], resolveMX['resolver'], resolveMX['status'], resolveMX['data']))

                    conn.execute('''INSERT INTO dns_records
                                     (date_time, domain_name, record_type, resolver, status, data)
                                     VALUES (?, ?, ?, ?, ?, ?)''',
                                 (resolveTXT['date_time'], resolveTXT['domain_name'], resolveTXT['record_type'], resolveTXT['resolver'], resolveTXT['status'], resolveTXT['data']))

                 
                    conn.execute('''INSERT INTO dns_records
                                     (date_time, domain_name, record_type, resolver, status, data)
                                     VALUES (?, ?, ?, ?, ?, ?)''',
                                 (resolveCNAME['date_time'], resolveCNAME['domain_name'], resolveCNAME['record_type'], resolveCNAME['resolver'], resolveCNAME['status'], resolveCNAME['data']))
                 
                    conn.execute('''INSERT INTO dns_records
                                     (date_time, domain_name, record_type, resolver, status, data)
                                     VALUES (?, ?, ?, ?, ?, ?)''',
                                 (resolveNS['date_time'], resolveNS['domain_name'], resolveNS['record_type'], resolveNS['resolver'], resolveNS['status'], resolveNS['data']))

                    conn.execute('''INSERT INTO dns_records
                                     (date_time, domain_name, record_type, resolver, status, data)
                                     VALUES (?, ?, ?, ?, ?, ?)''',
                                 (resolveSOA['date_time'], resolveSOA['domain_name'], resolveSOA['record_type'], resolveSOA['resolver'], resolveSOA['status'], resolveSOA['data']))
                
                    conn.execute('''INSERT INTO dns_records
                                     (date_time, domain_name, record_type, resolver, status, data)
                                     VALUES (?, ?, ?, ?, ?, ?)''',
                                 (resolvePTR['date_time'], resolvePTR['domain_name'], resolvePTR['record_type'], resolvePTR['resolver'], resolvePTR['status'], resolvePTR['data']))
                 
                    conn.execute('''INSERT INTO dns_records
                                     (date_time, domain_name, record_type, resolver, status, data)
                                     VALUES (?, ?, ?, ?, ?, ?)''',
                                 (resolveSRV['date_time'], resolveSRV['domain_name'], resolveSRV['record_type'], resolveSRV['resolver'], resolveSRV['status'], resolveSRV['data']))

                    conn.execute('''INSERT INTO dns_records
                                     (date_time, domain_name, record_type, resolver, status, data)
                                     VALUES (?, ?, ?, ?, ?, ?)''',
                                 (resolveCAA['date_time'], resolveCAA['domain_name'], resolveCAA['record_type'], resolveCAA['resolver'], resolveCAA['status'], resolveCAA['data']))
                
                conn.commit()

                if not suspended_mode:
                    break

                time.sleep(10)

            conn.close()
        except KeyboardInterrupt:
            print("\nCtrl+C pressed. Exiting...")
            exit(0)
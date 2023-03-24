#!/usr/bin/env python3

import time 
import json
import sqlite3
import os, sys
from datetime import datetime
from lib.dnsresolver import domaininfo

class makefile(object):

    def __init__(self):
        super(makefile, self).__init__()
        self.date = datetime.now().strftime('%Y-%m-%d|%H:%M:%S')
        self.file = open(os.path.join("Domain_list", "dns_domains.txt"))


    def single(self, url, dns, json=True):
        domain_object  = domaininfo(url, dns)
        if json == False:
            resolveA = domain_object.resolveA(json_format=False)
            resolveAAAA = domain_object.resolveAAAA(json_format=False)
            resolveMX = domain_object.resolveMX(json_format=False)
            resolveTXT = domain_object.resolveTXT(json_format=False)
            resolveCNAME = domain_object.resolveCNAME(json_format=False)
            resolveNS = domain_object.resolveNS(json_format=False)
            resolveSOA = domain_object.resolveSOA(json_format=False)

        else:
            resolveA = domain_object.resolveA(json_format=True)
            resolveAAAA = domain_object.resolveAAAA(json_format=True)
            resolveMX = domain_object.resolveMX(json_format=True)
            resolveTXT = domain_object.resolveTXT(json_format=True)
            resolveCNAME = domain_object.resolveCNAME(json_format=True)
            resolveNS = domain_object.resolveNS(json_format=True)
            resolveSOA = domain_object.resolveSOA(json_format=True)
        os.makedirs("Output", exist_ok=True)
        file = open(os.path.join("Output", self.date + ".txt"), "a")
        file.write("%s\n%s\n%s\n%s\n%s\n%s\n%s\n" % (
                                                    str(resolveA), 
                                                    str(resolveAAAA),
                                                    str(resolveMX), 
                                                    str(resolveTXT), 
                                                    str(resolveCNAME), 
                                                    str(resolveNS), 
                                                    str(resolveSOA))
                                                    )
        file.close()


    def bulk(self, dns, json=True):
        for url in self.file:
            url = url.strip()   
            domain_object = domaininfo(url, dns)
            if json == False:
                resolveA = domain_object.resolveA(json_format=False)
                resolveAAAA = domain_object.resolveAAAA(json_format=False)
                resolveMX = domain_object.resolveMX(json_format=False)
                resolveTXT = domain_object.resolveTXT(json_format=False)
                resolveCNAME = domain_object.resolveCNAME(json_format=False)
                resolveNS = domain_object.resolveNS(json_format=False)
                resolveSOA = domain_object.resolveSOA(json_format=False)
            else:
                resolveA = domain_object.resolveA(json_format=True)
                resolveAAAA = domain_object.resolveAAAA(json_format=True)
                resolveMX = domain_object.resolveMX(json_format=True)
                resolveTXT = domain_object.resolveTXT(json_format=True)
                resolveCNAME = domain_object.resolveCNAME(json_format=True)
                resolveNS = domain_object.resolveNS(json_format=True)
                resolveSOA = domain_object.resolveSOA(json_format=True)
            os.makedirs("Output", exist_ok=True)
            file = open(os.path.join("Output", self.date + ".txt"), "a")
            file.write("%s\n%s\n%s\n%s\n%s\n%s\n%s\n" % (
                                                        str(resolveA), 
                                                        str(resolveAAAA),
                                                        str(resolveMX), 
                                                        str(resolveTXT), 
                                                        str(resolveCNAME), 
                                                        str(resolveNS), 
                                                        str(resolveSOA))
                                                        )
            file.close()


    def database(self, dns):
        conn = sqlite3.connect('resolver.db')

        conn.execute('''CREATE TABLE IF NOT EXISTS dns_records
                         (date_time TEXT, domain_name TEXT, record_type TEXT,
                          resolver TEXT, status TEXT, data TEXT)''')

        for url in self.file:
            url = url.strip()
            domain_object  = domaininfo(url, dns)
            resolveA = domain_object.resolveA(json_format=False)
            resolveAAAA = domain_object.resolveAAAA(json_format=False)
            resolveMX = domain_object.resolveMX(json_format=False)
            resolveTXT = domain_object.resolveTXT(json_format=False)
            resolveCNAME = domain_object.resolveCNAME(json_format=False)
            resolveNS = domain_object.resolveNS(json_format=False)
            resolveSOA = domain_object.resolveSOA(json_format=False)
            

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


        conn.commit()
        conn.close()
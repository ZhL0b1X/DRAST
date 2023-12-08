#!/usr/bin/env python3

import json
import time
import os, sys
import requests
import animation
import dns.resolver
from datetime import datetime



class Domaininfo(object):

    def __init__(self, url, resolver_ip):
        super(Domaininfo, self).__init__()
        self.url   = url
        self.A     = []
        self.MX    = []
        self.NS    = []
        self.SOA   = []
        self.PTR   = []
        self.SRV   = []
        self.CAA   = []
        self.TXT   = []
        self.AAAA  = []
        self.CNAME = []
        self.GeoIP = 'https://geolocation-db.com/jsonp/'
        self.time  = datetime.now().strftime('%Y-%m-%dT%H:%M:%S.%f%z')
        self.resolver = resolver_ip.nameservers[0]
        try:
            answers = resolver_ip.resolve(self.url, 'A')
            self.A  = [rdata.address for rdata in answers]
        except dns.resolver.NXDOMAIN:
            self.A_error = "NXDOMAIN"
        except dns.resolver.NoNameservers:
            self.A_error = "NoNameservers"
        except dns.resolver.NoAnswer:
            self.A_error = "NoAnswer"
        except dns.exception.Timeout:
            self.A_error = "Timeout" 
        except:
            self.A = None
        try:
            answers = resolver_ip.resolve(self.url, 'NS')
            for rdata in answers:
                self.NS.append(rdata.to_text)
        except dns.resolver.NXDOMAIN:
            self.NS_error = "NXDOMAIN"
        except dns.resolver.NoNameservers:
            self.NS_error = "NoNameservers"
        except dns.resolver.NoAnswer:
            self.NS_error = "NoAnswer"
        except dns.exception.Timeout:
            self.NS_error = "Timeout"
        except:
            self.NS = None
        try:
            answers = resolver_ip.resolve(self.url, 'MX')
            for rdata in answers:
                self.MX.append(rdata.exchange)
        except dns.resolver.NXDOMAIN:
            self.MX_error = "NXDOMAIN"
        except dns.resolver.NoNameservers:
            self.MX_error = "NoNameservers"
        except dns.resolver.NoAnswer:
            self.MX_error = "NoAnswer"
        except dns.exception.Timeout:
            self.MX_error = "Timeout"
        except: 
            self.MX = None
        try: 
            answers = resolver_ip.resolve(self.url, 'AAAA')
            for rdata in answers:
                self.AAAA.append(rdata.address)
        except dns.resolver.NXDOMAIN:
            self.AAAA_error = "NXDOMAIN"
        except dns.resolver.NoNameservers:
            self.AAAA_error = "NoNameservers"
        except dns.resolver.NoAnswer:
            self.AAAA_error = "NoAnswer"
        except dns.exception.Timeout:
            self.AAAA_error = "Timeout" 
        except: 
            self.AAAA = None
        try: 
            answers = resolver_ip.resolve(self.url, 'CNAME')
            for rdata in answers:
                self.CNAME.append(rdata.target)
        except dns.resolver.NXDOMAIN:
            self.CNAME_error = "NXDOMAIN"
        except dns.resolver.NoNameservers:
            self.CNAME_error = "NoNameservers"
        except dns.resolver.NoAnswer:
            self.CNAME_error = "NoAnswer"
        except dns.exception.Timeout:
            self.CNAME_error = "Timeout"
        except: 
            self.CNAME = None
        try: 
            answers = resolver_ip.resolve(self.url, 'TXT')
            for rdata in answers:
                self.TXT.append(rdata)
        except dns.resolver.NXDOMAIN:
            self.TXT_error = "NXDOMAIN"
        except dns.resolver.NoNameservers:
            self.TXT_error = "NoNameservers"
        except dns.resolver.NoAnswer:
            self.TXT_error = "NoAnswer"
        except dns.exception.Timeout:
            self.TXT_error = "Timeout"
        except: 
            self.TXT = None
        try: 
            answers = resolver_ip.resolve(self.url, 'SOA')
            for rdata in answers:
                self.SOA.append(rdata)
        except dns.resolver.NXDOMAIN:
            self.SOA_error = "NXDOMAIN"
        except dns.resolver.NoNameservers:
            self.SOA_error = "NoNameservers"
        except dns.resolver.NoAnswer:
            self.SOA_error = "NoAnswer"
        except dns.exception.Timeout:
            self.SOA_error = "Timeout"
        except: 
            self.SOA = None
        try: 
            answers = resolver_ip.resolve(self.url, 'PTR')
            for rdata in answers:
                self.PTR.append(rdata.target)
        except dns.resolver.NXDOMAIN:
            self.PTR_error = "NXDOMAIN"
        except dns.resolver.NoNameservers:
            self.PTR_error = "NoNameservers"
        except dns.resolver.NoAnswer:
            self.PTR_error = "NoAnswer"
        except dns.exception.Timeout:
            self.PTR_error = "Timeout"
        except: 
            self.PTR = None
        try: 
            answers = resolver_ip.resolve(self.url, 'SRV')
            for rdata in answers:
                self.SRV.append(rdata)
        except dns.resolver.NXDOMAIN:
            self.SRV_error = "NXDOMAIN"
        except dns.resolver.NoNameservers:
            self.SRV_error = "NoNameservers"
        except dns.resolver.NoAnswer:
            self.SRV_error = "NoAnswer"
        except dns.exception.Timeout:
            self.SRV_error = "Timeout"
        except: 
            self.SRV = None
        try: 
            answers = resolver_ip.resolve(self.url, 'CAA')
            for rdata in answers:
                self.CAA.append(rdata)
        except dns.resolver.NXDOMAIN:
            self.CAA_error = "NXDOMAIN"
        except dns.resolver.NoNameservers:
            self.CAA_error = "NoNameservers"
        except dns.resolver.NoAnswer:
            self.CAA_error = "NoAnswer"
        except dns.exception.Timeout:
            self.CAA_error = "Timeout"
        except: 
            self.CAA = None

    def Geo_ip(self):
        data = []
        for ip in self.A:
            try:
                response = requests.get(self.GeoIP + ip)
                result   = response.content.decode()
                result   = result.split("(")[1].strip(")")
                result   = json.loads(result)
                if result["city"] == None:  
                    data.append({"IPV4": ip, 
                                 "Country": str(result["country_name"])})
                else:
                    data.append({"IPV4": ip,
                                 "Country": str(result["country_name"]),    
                                 "City":str(result["city"])})
            except (json.decoder.JSONDecodeError, 
                    requests.exceptions.ConnectionError):
                time.sleep(4)
        return data


    def resolveA(self, json_format=True):
        if self.A:
            A    =  {"date_time": self.time,
                     "domain_name": self.url,
                     "record_type": "A",
                     "resolver": self.resolver,
                     "status": "OK",
                     "data": self.Geo_ip()}
        else:
            A    =  {"date_time": self.time,
                     "domain_name": self.url,
                     "record_type": "A",
                     "resolver": self.resolver,
                     "status": self.A_error,
                     "data": ""}
        if json_format == False:
            return A
        else:
            json_object = json.dumps(A, indent = 10)    
            return json_object
    
    def resolveAAAA(self, json_format=True):
        if self.AAAA:
            AAAA =  {"date_time": self.time,
                     "domain_name": self.url,
                     "record_type": "AAAA",
                     "resolver": self.resolver,
                     "status": "OK",
                     "data": str(self.AAAA)}
        else:   
            AAAA =  {"date_time": self.time,
                     "domain_name": self.url,
                     "record_type": "AAAA",
                     "resolver": self.resolver,
                     "status": self.AAAA_error,
                     "data": ""}
        if json_format == False:
            return AAAA
        else:
            json_object = json.dumps(AAAA, indent = 10) 
            return json_object

    def resolveMX(self, json_format=True):
        if self.MX:             
            MX   =  {"date_time": self.time,
                     "domain_name": self.url,
                     "record_type": "MX",
                     "resolver": self.resolver,
                     "status": "OK",
                     "data": str(self.MX)}
        else:
            MX   =  {"date_time": self.time,
                     "domain_name": self.url,
                     "record_type": "MX",
                     "resolver": self.resolver,
                     "status": self.MX_error,
                     "data": ""}
        if json_format == False:
            return MX
        else:
            json_object = json.dumps(MX, indent = 10)   
            return json_object

    def resolveTXT(self, json_format=True):              
        if self.TXT:    
            TXT  =  {"date_time": self.time,
                     "domain_name": self.url,
                     "record_type": "TXT",
                     "resolver": self.resolver,
                     "status": "OK",
                     "data": str(self.TXT)}
        else:           
            TXT  =  {"date_time": self.time,
                     "domain_name": self.url,
                     "record_type": "TXT",
                     "resolver": self.resolver,
                     "status": self.TXT_error,
                     "data": ""}
        if json_format == False:
            return TXT
        else:
            json_object = json.dumps(TXT, indent = 10)  
            return json_object

    def resolveCNAME(self, json_format=True):                
        if self.CNAME:
            CNAME = {"date_time": self.time,
                     "domain_name": self.url,
                     "record_type": "CNAME",
                     "resolver": self.resolver,
                     "status": "OK",
                     "data": str(self.CNAME)}
        else:
            CNAME = {"date_time": self.time,
                     "domain_name": self.url,
                     "record_type": "CNAME",
                     "resolver": self.resolver,
                     "status": self.CNAME_error,
                     "data": ""}
        if json_format == False:
            return CNAME
        else:
            json_object = json.dumps(CNAME, indent = 10)    
            return json_object

    def resolveNS(self, json_format=True):                   
        if self.NS:
            NS  =   {"date_time": self.time,
                     "domain_name": self.url,
                     "record_type": "NS",
                     "resolver": self.resolver,
                     "status": "OK",
                     "data": str(self.NS)}
        else:
            NS  =   {"date_time": self.time,
                     "domain_name": self.url,
                     "record_type": "NS",
                     "resolver": self.resolver,
                     "status": self.NS_error,
                     "data": ""}
        if json_format == False:
            return NS
        else:
            json_object = json.dumps(NS, indent = 10)   
            return json_object

    def resolveSOA(self, json_format=True):
        if self.SOA:
            SOA  =   {"date_time": self.time,
                     "domain_name": self.url,
                     "record_type": "SOA",
                     "resolver": self.resolver,
                     "status": "OK",
                     "data": str(self.SOA)}
        else:
            SOA  =   {"date_time": self.time,
                     "domain_name": self.url,
                     "record_type": "SOA",
                     "resolver": self.resolver,
                     "status": self.SOA_error,
                     "data": ""}
        if json_format == False:
            return SOA
        else:
            json_object = json.dumps(SOA, indent = 10)  
            return json_object

    def resolvePTR(self, json_format=True):                
        if self.PTR:
            PTR = {"date_time": self.time,
                     "domain_name": self.url,
                     "record_type": "PTR",
                     "resolver": self.resolver,
                     "status": "OK",
                     "data": str(self.PTR)}
        else:
            PTR = {"date_time": self.time,
                     "domain_name": self.url,
                     "record_type": "PTR",
                     "resolver": self.resolver,
                     "status": self.PTR_error,
                     "data": ""}
        if json_format == False:
            return PTR
        else:
            json_object = json.dumps(PTR, indent = 10)    
            return json_object

    def resolveSRV(self, json_format=True):                   
        if self.SRV:
            SRV  =   {"date_time": self.time,
                     "domain_name": self.url,
                     "record_type": "SRV",
                     "resolver": self.resolver,
                     "status": "OK",
                     "data": str(self.SRV)}
        else:
            SRV  =   {"date_time": self.time,
                     "domain_name": self.url,
                     "record_type": "SRV",
                     "resolver": self.resolver,
                     "status": self.SRV_error,
                     "data": ""}
        if json_format == False:
            return SRV
        else:
            json_object = json.dumps(SRV, indent = 10)   
            return json_object

    def resolveCAA(self, json_format=True):
        if self.CAA:
            CAA  =   {"date_time": self.time,
                     "domain_name": self.url,
                     "record_type": "CAA",
                     "resolver": self.resolver,
                     "status": "OK",
                     "data": str(self.CAA)}
        else:
            CAA  =   {"date_time": self.time,
                     "domain_name": self.url,
                     "record_type": "CAA",
                     "resolver": self.resolver,
                     "status": self.CAA_error,
                     "data": ""}
        if json_format == False:
            return CAA
        else:
            json_object = json.dumps(CAA, indent = 10)  
            return json_object

def main():
    message = "This is a module!"
    print(message)

if __name__ == '__main__':
    main()

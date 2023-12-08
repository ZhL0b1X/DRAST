#!/usr/bin/env python3

import json
import time
import requests
import dns.resolver
import dns.exception
from datetime import datetime

class DomainInfo:
    def __init__(self, url, resolver_ip):
        self.url = url
        self.resolver = resolver_ip.nameservers[0]
        self.time = datetime.now().strftime('%Y-%m-%dT%H:%M:%S.%f%z')
        self.record_types = ['A', 'MX', 'NS', 'SOA', 'PTR', 'SRV', 'CAA', 'TXT', 'AAAA', 'CNAME']
        self.records = {rtype: [] for rtype in self.record_types}
        self.errors = {rtype: None for rtype in self.record_types}
        self.GeoIP = 'https://geolocation-db.com/jsonp/'
        for rtype in self.record_types:
            try:
                answers = resolver_ip.resolve(self.url, rtype)
                self.records[rtype] = [rdata.to_text() for rdata in answers]
            except dns.exception.DNSException as e:
                self.errors[rtype] = type(e).__name__

    def Geo_ip(self):
        data = []
        for ip in self.records['A']:
            try:
                response = requests.get(self.GeoIP + ip)
                result = response.content.decode()
                result = result.split("(")[1].strip(")")
                result = json.loads(result)
                data.append({"IPV4": ip, "Country": str(result.get("country_name")), "City": str(result.get("city"))})
            except Exception:
                time.sleep(4)
        return data

    def resolve(self, record_type, json_format=True):
        record_data = self.records.get(record_type, [])
        error = self.errors.get(record_type)
        response = {"date_time": self.time, "domain_name": self.url, "record_type": record_type,
                    "resolver": self.resolver, "status": "OK" if record_data else error,
                    "data": self.Geo_ip() if record_type == 'A' else str(record_data)}
        return json.dumps(response, indent=10) if json_format else response

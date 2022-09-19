import time 
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
			json_data = domain_object.json_generator(json_format=False)
		else:
			json_data = domain_object.json_generator(json_format=True)
		os.makedirs("Output", exist_ok=True)
		file = open(os.path.join("Output", self.date + ".txt"), "a")
		file.write(str(json_data))
		file.close()


	def bulk(self, dns, json=True):
		for url in self.file:
			url = url.strip()	
			domain_object = domaininfo(url, dns)
			if json == False:
				json_data = domain_object.json_generator(json_format=False)
			else:
				json_data = domain_object.json_generator(json_format=True)
			os.makedirs("Output", exist_ok=True)
			file = open(os.path.join("Output", self.date + ".txt"), "a")
			file.write(str(json_data))
			file.close()


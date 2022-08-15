import time 
import os, sys
import animation
import dns.resolver
from datetime import datetime
from lib.DomainInfo import DomainInfo



if __name__ == "__main__":
	Date         = datetime.now().strftime('%Y-%m-%d|%H:%M:%S')
	Domians_file = open(os.path.join("Domain_list", "dns_domains.txt"))
	while True:
		try:
			Default_DNS  = dns.resolver.Resolver()
			Input_DNS    = [input('Enter DNS ip or press "Enter" to use the default IP:  ')] 
			if Input_DNS == [""]:
				Default_DNS
			else:
				Default_DNS.nameservers = Input_DNS
		except ValueError:
			print("Invalid DNS ip.\n"
				  "Please try again")
			continue
		break
	os.system('cls' if os.name == 'nt' else 'clear')
	wait_animation = animation.Wait(color="green", speed=0.8)
	wait_animation.start()
	for url in Domians_file:
		url = url.strip()	
		domain_object = DomainInfo(url, Default_DNS)
		json_data = domain_object.JSON_generator(json_format=True)
		os.makedirs("Output", exist_ok=True)
		file = open(os.path.join("Output", Date + ".txt"), "a")
		file.write(str(json_data))
		file.close()
	wait_animation.stop()
	print("Data saved")
	time.sleep(1.5)
	os.system('cls' if os.name == 'nt' else 'clear')	







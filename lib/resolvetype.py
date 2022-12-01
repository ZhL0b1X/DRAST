#!/usr/bin/env python3

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
            resolveA = domain_object.resolveA(json_format=False)
            resolverAAAA = domain_object.resolverAAAA(json_format=False)
            resolveMX = domain_object.resolveMX(json_format=False)
            resolveTXT = domain_object.resolveTXT(json_format=False)
            resolveCNAME = domain_object.resolveCNAME(json_format=False)
            resolveNS = domain_object.resolveNS(json_format=False)
            resolveSOA = domain_object.resolveSOA(json_format=False)

        else:
            resolveA = domain_object.resolveA(json_format=True)
            resolverAAAA = domain_object.resolverAAAA(json_format=True)
            resolveMX = domain_object.resolveMX(json_format=True)
            resolveTXT = domain_object.resolveTXT(json_format=True)
            resolveCNAME = domain_object.resolveCNAME(json_format=True)
            resolveNS = domain_object.resolveNS(json_format=True)
            resolveSOA = domain_object.resolveSOA(json_format=True)
        os.makedirs("Output", exist_ok=True)
        file = open(os.path.join("Output", self.date + ".txt"), "a")
        file.write("%s\n%s\n%s\n%s\n%s\n%s\n%s\n" % (
                                                    str(resolveA), 
                                                    str(resolverAAAA),
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
                resolverAAAA = domain_object.resolverAAAA(json_format=False)
                resolveMX = domain_object.resolveMX(json_format=False)
                resolveTXT = domain_object.resolveTXT(json_format=False)
                resolveCNAME = domain_object.resolveCNAME(json_format=False)
                resolveNS = domain_object.resolveNS(json_format=False)
                resolveSOA = domain_object.resolveSOA(json_format=False)
            else:
                resolveA = domain_object.resolveA(json_format=True)
                resolverAAAA = domain_object.resolverAAAA(json_format=True)
                resolveMX = domain_object.resolveMX(json_format=True)
                resolveTXT = domain_object.resolveTXT(json_format=True)
                resolveCNAME = domain_object.resolveCNAME(json_format=True)
                resolveNS = domain_object.resolveNS(json_format=True)
                resolveSOA = domain_object.resolveSOA(json_format=True)
            os.makedirs("Output", exist_ok=True)
            file = open(os.path.join("Output", self.date + ".txt"), "a")
            file.write("%s\n%s\n%s\n%s\n%s\n%s\n%s\n" % (
                                                        str(resolveA), 
                                                        str(resolverAAAA),
                                                        str(resolveMX), 
                                                        str(resolveTXT), 
                                                        str(resolveCNAME), 
                                                        str(resolveNS), 
                                                        str(resolveSOA))
                                                        )
            file.close()



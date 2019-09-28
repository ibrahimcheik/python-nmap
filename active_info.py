#!/usr/bin/env python
import nmap
import sys
import pprint

nm_scan = nmap.PortScanner()
nm_scanner = nm_scan.scan('198.49.23.145','443',arguments='-O')
pprint.pprint(nm_scanner)
print("the host is "+nm_scanner['scan']['198.49.23.145']['status']['state'])
print("the port 443 is : "+nm_scanner['scan']['198.49.23.145']['tcp'][443]['state'])
print("the scanning method is : "+nm_scanner['scan']['198.49.23.145']['tcp'][443]['reason'])
print("there is %s percent the host is running %s"%(nm_scanner['scan']['198.49.23.145']['osmatch'][0]['accuracy'],nm_scanner['scan']['198.49.23.145']['osmatch'][0]['name']))


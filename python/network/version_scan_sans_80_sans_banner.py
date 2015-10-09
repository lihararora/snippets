# Assumes that the masscan list output has been stored in the file test.list 
import os

with open('test.list') as f:
	contents = f.readlines()

for l in contents:
	a = l.split()
	if len(a) > 2:
		ip = a[3]
		port = a[2]
		if port != '80':
			os.system('nmap --max-retries 10 --max-scan-delay 0 --min-parallelism 10 --max-parallelism 10 --min-rtt-timeout 50ms --max-rtt-timeout 50ms -sV -v -p '+port+' '+ip+ ' | tee -a test_version_sans_80_sans_banner.nmap')

	


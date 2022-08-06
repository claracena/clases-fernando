import nmap
# from nmap import PortScanner

host= input("[+] Ingrese la IP objetivo: ")
nm= nmap.PortScanner()
puertos_abiertos="-p"
count=0
results= nm.scan(host)

print(f"Host : {host}")
try:
	print(f"State : {nm[host].state()}")
except Exception as e:
	print(type(e).__name__)
for proto in nm[host].all_protocols():
	print("Protocol : %s" % proto)
	lport = nm[host][proto].keys()
	sorted(lport)
	for port in lport:
		print ("port : %s\tstate : %s" % (port, nm[host][proto][port]["state"]))
		if count==0:
			puertos_abiertos= puertos_abiertos+" "+str(port)
		else:
			puertos_abiertos=puertos_abiertos+","+str(port)

print("\nPuertos abiertos: " +puertos_abiertos+" "+str(host))

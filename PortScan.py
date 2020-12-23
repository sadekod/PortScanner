
import socket
import subprocess
import pyfiglet
import sys
from datetime import datetime
subprocess.call('cls', shell=True)
ascii_banner = pyfiglet.figlet_format("PORT SCANNER ",font = "slant")
ascii_banner+=pyfiglet.figlet_format("By Kadir", font="digital")
print(ascii_banner)
remoteServer    = input("Please Enter the Host to Scan: ")
StartScanPort=int(input("Please Enter Start Port..."))
StopScanPort=int(input("Please Enter End Port..."))
remoteServerIP  = socket.gethostbyname(remoteServer)
print ("-" * 60)
print ("Please Wait, the specified host is scanning:", remoteServerIP)
print ("-" * 60)
t1 = datetime.now()
try:
    for port in range(StartScanPort,StopScanPort+1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((remoteServerIP, port))
        if result == 0:
            print ("Port {}: 	 Open".format(port), socket.getservbyport(port),"\n")
        sock.close()

except KeyboardInterrupt:
    print ("You pressed Ctrl+C")
    sys.exit()

except socket.gaierror:
    print ('Hostname could not be resolved. Exiting')
    sys.exit()

except socket.error:
    print ("Couldn't connect to server")
    sys.exit()

t2 = datetime.now()
total =  t2 - t1


print ('Port scan complete: ', total)

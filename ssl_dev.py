
 
import socket
import sys
import time
from tcp_client import tcp_client
from udp_client import udp_client



udp = input("Do you want to UDP?   ")
if udp == 'yes':
    udp_client()
else:
     tcp_client()
     









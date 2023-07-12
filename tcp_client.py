import socket
import sys
from paddng import padit


def tcp_client():

    while True: 

        HOST, PORT = "129.243.21.242", 2323
        data = padit(b'TCP_TESTERONI', 1420)



        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
       

            
            s.connect((HOST, PORT))
            s.sendto(bytes(data), (HOST, PORT))
            print("Sent:     {}".format(data))

            
if __name__ == "__main__":
    tcp_client() 
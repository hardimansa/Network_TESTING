import socket
import sys
import unicodedata
from paddng import padit


def udp_client():


    while True:
        with open("backup.192.168.56.12", "r") as config:
                lines = config.read().rstrip()


        HOST, PORT = "129.243.21.242", 2323
        #data = lines
        data = padit(b'teseroni', 1311)






        # Create a socket (SOCK_STREAM means a TCP socket)
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

            # Connect to server and send data
            # sock.connect((HOST, PORT))

        # while True: 
                

        #sock.sendto(bytes(data, "utf-8"), (HOST, PORT))
        sock.sendto(bytes(data), (HOST,PORT))
            


        print("Sent:     {}".format(data))


if __name__ == "__main__":
    udp_client()
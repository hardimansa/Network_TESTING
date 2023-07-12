import socket
from tcp import MyTCPHandler
import socketserver
import select



def alt():
    alt_host = '129.243.21.242'
    alt_port = 2323

    alt_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    alt_server_address = (alt_host, alt_port)
    alt_sock.bind(alt_server_address)
    print('UDP server started {}:{}'.format(alt_host,alt_port))
    alt_sock_clients = [alt_sock]


    while True:
        readable, _, _ = select.select(alt_sock_clients, [], [])
        for sock in readable:
            if sock is alt_sock:
                data, address = alt_sock.recvfrom(131768)
                
                print('rx data:', data.decode())
                print('Client address:', address)
                with open("newnew.txt", "a") as new:
                    new.write(data.decode())

                # sys.exit()
                     


     
def tcp2():
       
       
        HOST, PORT = "129.243.21.242", 2323
        print('TCP server started {}:{}'.format(HOST,PORT))
        with socketserver.TCPServer((HOST, PORT), MyTCPHandler) as server:
                  server.serve_forever()
 

               


udp = input("RU4UDP?    ")

if udp == "yes":
     alt()
else:
    print("TCP it is!")
    tcp2()
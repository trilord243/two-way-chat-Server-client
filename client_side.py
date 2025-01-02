#Client side

import socket



#Define variables
dest_ip=socket.gethostbyname(socket.gethostname())
dest_port=5037
encoder="utf-8"
bytes_size=1024


#Create socket IPV4  (AF_INET), and TCP/IP (SOCK_STREAM)

client_socket= socket.socket(socket.AF_INET,socket.SOCK_STREAM)


client_socket.connect( (dest_ip,dest_port))
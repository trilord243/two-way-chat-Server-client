#Sever Side

import socket

#Define constants

host_ip=socket.gethostbyname(socket.gethostname())

host_port=5037

encoder="utf-8"

byte_size=1024

#Create server socket IPV4 (AF_INET), TCP/IP (SOCK_STREAM)
server_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#Bind and listen

server_socket.bind( (host_ip,host_port) )

server_socket.listen()

#Accept incoming connection and they are connecter

print(f"Server is running ... in {host_ip}:{host_port} \n ")

client_socket,client_address=server_socket.accept()

client_socket.send("You are connected...\n".encode(encoder))

#Send recieve messages

while True:
    #Recieve information
    message=client_socket.recv(byte_size).decode(encoder)

    #Quit if client wants to quit
    if message== "quit":
        client_socket.send("quit".encode(encoder))
        print("ending the chat...")
        break
    else:

        print(f"\n{message}")
        message=input("Message: ")
        client_socket.send(message.encode(encoder))



client_socket.close()
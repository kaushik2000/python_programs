# Create a socket to access a web-page through PORT:80 (HTTP)
import socket

my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
my_socket.connect( ('data.pr4e.org', 80) )

print('Connection successful')
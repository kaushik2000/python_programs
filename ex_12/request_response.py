# Using socket(), A connection can be made using connect(), encode(), send(), recv(), decode() & close() methods, thus extracting data.
# Output similar to that of 'telnet' is received

# Establish socket
import socket
my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Establish connection
domain = "data.pr4e.org"
try:
    my_socket.connect( (domain, 80) )
except:
    print('Domain doesn\'t exist:', domain)
    quit()
print('>>>> Connection successful')

# Sending a GET request. The 2nd part includes complete url-directory of the file.
# The 3rd part of the string described the prototcol version + two carriage return & new line characters similar to telnet
doc_cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode() # Encoding the sent data
my_socket.send(doc_cmd)
print('>>>> Request sent')

# Receiving the required file data
#count = 0
while True:
    data = my_socket.recv(512) # 512 is the buffer_size. At a time the socket receives 512 characters
    if len(data) < 1 : break
    #count += 1
    #print('>>>> Requect cycle number:', count)
    print(data.decode())
print('>>>> Data extracted successfully')

# Closing the connection
my_socket.close()
print('>>>> Connection terminated')

'''
The cycle for rquesting data is as follows:

socket()
    connect()
        encode() - send() - recv() - decode()
    close()
'''
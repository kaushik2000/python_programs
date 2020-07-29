# Using socket(), A connection can be made using connect(), encode(), send(), recv(), decode() & close() methods, thus extracting data.
'''
The cycle for rquesting data is as follows:

socket()
    connect()
        encode() - send() - recv() - decode()
    close()
'''
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
print('>>>> Connection successful to domain:', domain)

document = input('Enter the document name: ')

# Sending a GET request. The 2nd part includes complete url-directory of the file.
# The 3rd part of the string describes the prototcol version + two carriage return & new line characters (i.e. EOL-End Of Line) similar to telnet
doc_cmd = 'GET http://data.pr4e.org/' + document + ' HTTP/1.0\r\n\r\n'
doc_cmd = doc_cmd.encode() # Encoding the sent data (UNICODE to UTF-8)
my_socket.send(doc_cmd)
print('>>>> Request sent')

# Receiving the required file data
#count = 0
lines = str()
while True:
    data = my_socket.recv(512) # 512 is the buffer_size. At a time the socket receives 512 characters
    if len(data) < 1 : break
    #count += 1
    #print('>>>> Requect cycle number:', count)
    lines = lines + data.decode() # Converting UTF-8 to UNICODE for python
print(lines)
print('>>>> Data extracted successfully')

# Closing the connection
my_socket.close()
print('>>>> Connection terminated')

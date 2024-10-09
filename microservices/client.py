import socket
import sys

def client():
    '''a simple microservices client'''
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    port_t = ('localhost', 9874)
    client.connect(port_t) # we atempt to connect to our microservice server
    # if there are additional system argument variables, send them to the server
    if len(sys.argv) > 1: # we have arguments!
        message = ' '.join(sys.argv[1:]) # slice the sys.argv to leave off the zeroth member
    else:
        message = 'default'
    client.send(message.encode()) # we must encode as bytes
    # see if there is a response from the server
    data = client.recv(1024)
    print(f'Cleint received {data}')
    client.close()

if __name__ == '__main__':
    client()
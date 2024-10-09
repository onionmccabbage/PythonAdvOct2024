import socket

def client():
    '''a simple microservices client'''
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    port_t = ('localhost', 9874)
    client.connect(port_t) # we atempt to connect to our microservice server
    client.send(b'hello') # we must encode as bytes
    # see if there is a response from the server
    data = client.recv(1024)
    print(f'Cleint received {data}')
    client.close()

if __name__ == '__main__':
    client()
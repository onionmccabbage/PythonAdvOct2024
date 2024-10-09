import socket

def writeToFile(data):
    '''we can log every request buffer to a file'''
    with open('server_log','ab') as fout:
        fout.write(f'{data}\n')

def server():
    '''a microservice for http clients. 
    Here we echo whatever the client requests as upper-case'''
    port_t = ('localhost', 9874) # typically an IP address
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(port_t)
    # next we let our server begin to listen for requsts
    server.listen()
    print(f'Server is listening on {port_t[0]} port {port_t[1]}')
    # we ned the server to coninue to listen - a run loop
    while True:
        # unpack any client request
        (client, addr) = server.accept()
        print(f'Request received from {addr}')
        # read what the client request contains (a portion of the request)
        buf = client.recv(1024) # just the first 1024 bytes
        print(f'Server has received {buf}')
        # commit the buffer to a file
        writeToFile(buf)
        # echo back to the client
        client.send(buf.upper())
        # we no longer wish to interact with this client, so we close the connection
        client.close()
        # provide a means to quit the server
        if buf == b'quit':
            server.close()  # stop the server
            break # close the while loop

if __name__ == '__main__':
    # start running the server
    server()
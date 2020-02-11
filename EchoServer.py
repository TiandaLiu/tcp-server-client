import socket
import sys

# read port argument
port = int(sys.argv[1])

# create a socket and bind it to the server address and port
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('', port)
sock.bind(server_address)
sock.listen(5)
# print the server information
print("The server at {0} with port number: {1} is ready to receive: ".format(socket.gethostname(), port))

# listening
while True:
    # print("Waiting for a connection...")
    connection, client_address = sock.accept()
    print("New Connection!")
    # receive and print message
    message = connection.recv(2048).decode()
    print("Reveived message: {}".format(message))
    # resend message
    connection.send(message.encode())
    # close the connection
    connection.close()


import socket
import sys

# read the address and port argument
serverName, serverPort = sys.argv[1], int(sys.argv[2])

# sending message
while True:
    # read message from command line
    message = input()
    if not message:
        continue

    # create socket and send message
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((serverName, serverPort))
    sock.send(message.encode())

    # listen the response from server and print it to the STDOUT
    receivedMessage = sock.recv(2048).decode()
    print("Message reveived from {0}:{1}: {2}".format(serverName, serverPort, receivedMessage))

    # close the connection
    sock.close()
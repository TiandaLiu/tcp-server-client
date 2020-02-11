# TCP Server & Client

## Instruction

### To start the server, run following code in command line tools (terminal):
    $ python3 EchoServer.py <portNumber>
    (ex. python3 EchoServer.py 8880)

### To start the client, run following code in command line tools (terminal):
    $ python3 EchoClient.py <hostName> <portNumber>
    (ex. python3 EchoClient.py linux1.cs.uchicago.edu 8880)

## Demo
Setup server:

    $ python3 EchoServer.py 8080
    The server at TIANDAs-MacBook-Pro.local with port number: 8080 is ready to receive: 

Setup client:

    $ python3 EchoClient.py 127.0.0.1 8080

Send message from client to server:

    $ python3 EchoClient.py 127.0.0.1 8080
    > Hello Server!
    > Message reveived from 127.0.0.1:8080: hello

Reveive message from client and send response to client:

    $ python3 EchoServer.py 8080
    > The server at TIANDAs-MacBook-Pro.local with port      number: 8080 is ready to receive: 
    > New Connection!
    > Reveived message: Hello Server!
    > Responsed message: Hello Server!


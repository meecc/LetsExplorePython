
# 2. Socket Programming in Python 
---

Python provides support for both connection-oriented and connectionless protocols using low level sockets.

It also has libraries that provide higher-level access to specific application-level network protocols, such as FTP, HTTP & EMAIL etc.

## What is Sockets?
-----

Sockets are the endpoints of a bidirectional communications channel. Sockets may communicate within a process, between processes on the same machine, or between processes on different continents.

Sockets may be implemented over a number of different channel types: Unix domain sockets, TCP, UDP, and so on. The socket library provides specific classes for handling the common transports as well as a generic interface for handling the rest.

### The socket Module

To create a socket, you must use the socket.socket() function available in socket module, which has the general syntax −

```python
s = socket.socket (socket_family, socket_type, protocol=0)
```

socket_family: This is either AF_UNIX or AF_INET

socket_type: This is either SOCK_STREAM or SOCK_DGRAM.

#### Server Socket Methods

| Method | Description |
|--------|-------------|
| s.bind() |	This method binds address (hostname, port number pair) to socket.| 
| s.listen()	| This method sets up and start TCP listener.| 
| s.accept()| 	This passively accept TCP client connection, waiting until connection arrives (blocking).| 

#### Client Socket Methods

|Method	    | Description |
|-----------|-------------|
|s.connect() |	This method actively initiates TCP server connection. |

#### General Socket Methods

| Method	| Description| 
|-----------|------------|
| s.recv()	| This method receives TCP message| 
| s.send()	| This method transmits TCP message| 
| s.recvfrom()	| This method receives UDP message| 
| s.sendto()	| This method transmits UDP message| 
| s.close()	| This method closes socket| 
| socket.gethostname()	| Returns the hostname.| 

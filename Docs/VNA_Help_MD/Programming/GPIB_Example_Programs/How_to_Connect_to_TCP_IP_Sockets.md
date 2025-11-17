# How to Connect to TCP/IP Sockets

When connecting to TCP/IP sockets, it is important to enable the read
termination character, or read's will timeout.

Simply add the below code after you've established a connection to the
instrument:

if session.resource_name.endswith('SOCKET'):  session.read_termination = '\n'  
---


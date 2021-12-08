###############################################
# Group Name  : Tencent

# Member1 Name: Michael Bauers
# Member1 SIS ID: 831781483
# Member1 Login ID: mbauers

# Member2 Name: Mason Fout
# Member2 SIS ID: 831378374
# Member2 Login ID: mfout
###############################################

import sys
import os
import selectors
import threading
import types
import socket

sel = selectors.DefaultSelector()

host = socket.gethostname()
port = 1234

if len(sys.argv) > 3 or len(sys.argv) == 2:
    print("Incorrect number of arguments.")
    exit()

elif len(sys.argv) == 3 and sys.argv[1] != "-p":
    print("Incorrect format of arguments.")
    exit()

if len(sys.argv) == 3:
    port = sys.argv[2]

"""
#called when lsock receives a connection request from ss
def newConnRequest(sock):
    print("New connection request")
    conn, addr = sock.accept()
    conn.setblocking(False)
    data = types.SimpleNamespace(addr=addr, inb=b"", outb=b"")
    events = selectors.EVENT_READ | selectors.EVENT_WRITE
    sel.register(conn, events, data=data)

def connReady(key, mask):
    print("Connection ready")
    sock = key.fileobj
    data = key.data
    if mask & selectors.EVENT_READ:
        recv_data = sock.recv(1024)
        if recv_data:
            data.outb += recv_data
            print(f"data.outb: {data.outb}")
        else:
            print(f"Closing connection to {data.addr}")
            sel.unregister(sock)
            sock.close()
    if mask & selectors.EVENT_WRITE:
        if data.outb:
            print(f"Echoing {repr(data.outb)} to {data.addr}")
            sent = sock.send(data.outb)
            data.outb = data.outb[sent:]
"""

def sendNext():
    return

print(f"ss hostname: {host}")
print(f"ss port #: {port}")

#listening socket
lsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
lsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
lsock.bind(("127.0.0.1", int(port)))
print(f"Listening on port {port}")
lsock.listen()

while True:
    conn, addr = lsock.accept()
    fromClient = ''
    
    data = conn.recv(1024)
    fromClient += data.decode()
    print(f"fromClient: {fromClient}")

    firstPos = fromClient[fromClient.find("'")+1:]
    destURL = firstPos[:firstPos.find("'")]

"""

try:
    while True:
        sel.register(lsock, selectors.EVENT_READ, data=None)
        events = sel.select(timeout=None)
        print("Event selected")

        for key, mask in events:
            if key.data is None:
                newConnRequest(key.fileobj)
            else:
                connReady(key, mask)

except KeyboardInterrupt:
    print("Caught keyboard interrupt. Exiting.")
    exit()
finally:
    sel.close()

"""
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
import random
import os
from socket import *

if (len(sys.argv) != 2 and len(sys.argv) != 4):
    print("Incorrect number of arguments")
    exit()

elif(len(sys.argv) == 4 and sys.argv[2] != "-c"):
    print("Incorrect format of arguments")
    exit()

chainPath = ""

if (len(sys.argv) == 4):
    chainPath = sys.argv[3]
else:
    chainPath = "./chaingang.txt"
    # for root, dirs, files in os.walk("./"):
    #     if chainFile in files:
    #        chainPath = os.path.join(root, chainFile)
    #        break
    
    # if(chainPath == ""):
    #     print("Cannot find chaingang.txt")
    #     exit()

if ((sys.argv[1].rfind('/') == len(sys.argv[1]) - 1) or (sys.argv[1].rfind('/') == -1)):
    fileName = "index.html"
else:
    fileName = sys.argv[1][sys.argv[1].rfind('/'): len(sys.argv[1])]

def listToString(chainList):
    chainStr = ""
    for i in chainList:
        print(f"line: {chainList[i]}")
        chainStr += chainList[i]
    return chainStr

chainGang = []

try:
    with open(chainPath, "r") as f:
        chainGang = f.readlines()
        f.close()

    if (int(chainGang[0]) != len(chainGang) -1 or chainGang[0] == 0):
        print("File has either no addresses or a size mismatch.")
        exit()
except:
    print("Unable to read file.")
    exit()

print(f"chainGang[0]: {chainGang[0]}")
print(f"Request: {sys.argv[1]}")
print("Chainlist is")
chainList = ""

for i in range(len(chainGang)):
    if (i == 0):
        chainGang[i] = int(chainGang[i])
        continue
        
    address, port = chainGang[i].split(" ")
    port = port[0: int(port)]
    chainGang[i] = (address, int(port))
    chainList += str(chainGang[i]) + "\n"
    print(f"<{address}, {int(port)}>")

randomNum = random.randint(1, int(chainGang[0]))

address, port = chainGang[randomNum]

chainGang.pop(randomNum)
numSS = chainGang[0]
chainGang[0] = chainGang[0] - 1

print(f"Next SS is <{address},{int(port)}>")

chainGang.append(sys.argv[1])

try:
    s = socket(AF_INET, SOCK_STREAM)
    print(f"Connecting to {address}:{port}")
    s.connect_ex((address, int(port)))
    print("Connected")
    s.send(str(chainGang).encode())
    s.send(chainList.encode())
    print("Waiting for file")
    with open(fileName, 'w') as fp:
        while True:
            receive = s.recv(1024).decode()
            if(receive == ""):
                break
            fp.write(receive)
    print("Goodbye!")
    s.close()

except:
    print("Could not connect")
    s.close()
    exit()

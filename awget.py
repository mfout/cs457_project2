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

for i in range(len(chainGang)):
    if (i == 0):
        chainGang[i] = int(chainGang[i])
        continue
        
    address, port = chainGang[i].split(" ")
    port = port[0: len(port)]
    chainGang[i] = ((address, port))

randomNum = random.randint(1, int(chainGang[0]))

address, port = chainGang[randomNum]

print(f"Request: {sys.argv[1]}")
print("Chainlist is")
for i in range(len(chainGang)):
    print(chainGang[i])

chainGang.pop(randomNum)
chainGang[0] = chainGang[0] - 1

print(f"Next SS is <{address},{port}>")

chainGang.append(sys.argv[1])


try:
    s = socket(AF_INET, SOCK_STREAM)
    s.connect((address, int(port)))
    s.send(str(chainGang).encode())
    print("Waiting for file")
    with open(fileName, 'w') as fp:
        while True:
            receive = s.recv(1024).decode()
            if(receive == ""):
                break
            print("Relaying file")
            fp.write(receive)
    print("Goodbye!")
    s.close()

except:
    print("Could not connect")
    s.close()
    exit()

###############################################
# Group Name  : Tencent

# Member1 Name: Mason Fout
# Member1 SIS ID: 831378374
# Member1 Login ID: mfout

# Member2 Name: XXXXXX
# Member2 SIS ID: XXXXXX
# Member2 Login ID: XXXXXX
###############################################

import sys

#create a class?
#class

#url and optional chainfile name
init(sys.argv[1], sys.argv[2])

def init(url, chainFile="chaingang.txt"):
    readFile(chainFile)
    readURL(url)
                
def readFile(chainFile):
    filename = "chaingang.txt"
    try:
        if chainFile != filename:
            filename = chainFile

        with open(filename, 'r') as file:
            #lines is a list of strings for each line of the text
            lines = file.readlines()


    except:
        print("Local file ", filename, " not found. Exiting program.")
        sys.exit(1)

def readURL(url):
    

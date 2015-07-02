#!/usr/bin/env python

import sys

varstore = {}

def main():
    print("ParseBasic interpreter v0.1")
    print("Copyright 2015 NETponents")
    print("Licensed under MIT license")
    print("Commercial use of this build is prohibited")
    print("============================================")
    print(" ")
    print("Creating virtual filesystem")
    startpath = "./bootloader/bootloader.pba"
    if sys.argv[1] != "":
        startpath = sys.argv[1]
    startRead(startpath)
        
def startRead(filepath):
    print("Opened file " + filepath)
    fileHandle = open(filepath, 'r')
    fileHandle.seek(0)
    for line in fileHandle:
        line = line.replace(";", "").replace("/n", "").strip()
        if line.startswith("//"):
            # Do nothing, this is a comment
            print "Comment found"
        elif line.startswith("PRINT"):
            line = line.replace("PRINT", "").replace('"',"").strip()
            print line
        elif line.startswith("NEWPRINT"):
            print '\n'
        elif line.startswith("CREATESWAP"):
            print "Initialized SWAP space"
        elif line.startswith("IO"):
            cmds = line.split()
            print "IO port " + cmds[1] + " has a status of " + cmds[2]
        elif line.startswith("NEW"):
            cmds = line.split()
            try:
                varstore[cmds[1].replace("$","")]
                print "ERROR: variable " + cmds[1] + " already exists."
            except: 
                varstore[cmds[1].replace("$","")] = str(line.replace("NEW","").replace(cmds[1],"").strip())
                pass
        elif line.startswith("DELETE"):
            try:
                del varstore[line.split()[1].replace("$","").strip()]
            except:
                print "ERROR: variable " + line.split()[1] + " is not defined."
                pass
        elif line.startswith("SET"):
            try:
                varstore[line.split()[1].replace("$","").strip()] = line.replace("SET","").replace(line.split()[1],"").strip()
            except:
                print "ERROR: variable " + line.split()[1] + " is not defined."
        elif line.startswith("EXTLOAD"):
            startRead("." + line.replace("EXTLOAD","").strip())
        elif line.startswith("END"):
            print "Program has quit. Exiting."
            sys.exit(0)
        else:
            print "ERROR: Unknown command in file " + filepath
    fileHandle.close

if __name__ == '__main__':
    main()

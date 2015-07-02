#!/usr/bin/env python

import sys

varstore = {}

def main():
    print("ParseBasic interpreter v0.1")
    print("Copyright 2015 NETponents")
    print("Licensed under MIT license")
    print("Commercial use of this build is prohibited")
    print("Creating virtual filesystem")
    startpath = "/bootloader/bootloader.pba"
    if sys.argv[1] != "":
        startpath = sys.argv[1]
        
def startRead(filepath):
    print("Opened file " + filepath)
    fileHandle = open(filepath, 'r')
    fileHandle.seek(0)
    for line in fileHandle:
        line = line.replace(";", "").replace("/n", "").strip()
        if line.startswith("//"):
            # Do nothing, this is a comment
        else if line.startwith("PRINT"):
            line = line.replace("PRINT", "").replace('"',"").strip()
            print line
        else if line.startswith("NEWPRINT"):
            print '\n'
        else if line.startswith("CREATESWAP"):
            # Do nothing for now
        else if line.startswith("IO"):
            cmds = line.split()
            print "IO port " + cmds[1] + " has a status of " + cmds[2]
        else if line.startswith("NEW"):
            cmds = line.split()
            try:
                varstore[cmds[1].replace("$","")]
                print "ERROR: variable " + cmds[1] + " already exists."
            except: 
                varstore[cmds[1].replace("$","")] = str(line.replace("NEW","").replace(cmds[1],"").strip())
                pass
        else if line.startswith("DELETE"):
            try:
                del varstore[line.split()[1].replace("$","").strip()]
            except:
                print "ERROR: variable " + line.split()[1] + " is not defined."
                pass
        else if line.startswith("SET"):
            try:
                varstore[line.split()[1].replace("$","").strip()] = line.replace("SET","").replace(line.split()[1],"").strip()
            except:
                print "ERROR: variable " + line.split()[1] + " is not defined."
        else if line.startswith("EXTLOAD"):
            startRead(line.replace("EXTLOAD","").strip())
        else if line.startswith("END"):
            print "Program has quit. Exiting."
            sys.exit(0)
        else:
            print "ERROR: Unknown command in file " + filepath
    fileHandle.close

if __name__ == '__main__':
    main()

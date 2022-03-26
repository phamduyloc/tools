import sys
import os

filecontainIp = sys.argv[1]
print (filecontainIp)
fileoutput=sys.argv[2]

file1 = open(filecontainIp)
lines = file1.readlines()
count = 0
for line in lines:    
    if line[0:4]=="IP: ":   	
    	fileout = open(fileoutput,'a')
    	fileout.write(line[4:])
    	fileout.close()
    
    
    

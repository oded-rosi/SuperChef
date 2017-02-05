import commands
#ret = commands.getoutput("ping google.com")
#print ret
import os
import sys
import subprocess


#output = subprocess.Popen(["ping google.com",""],stdout=subprocess.PIPE).communicate()[0]
output  = os.popen("dir > c:\oded.txt",'w',-1)
print output
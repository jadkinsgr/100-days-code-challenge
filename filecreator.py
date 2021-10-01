import os

num = 0 
while num < 100:
    pdir = 'PythonScripts/100-days-code-challenge/Day'
    num += 1
    com = pdir+str(num)
    os.mkdir(com)

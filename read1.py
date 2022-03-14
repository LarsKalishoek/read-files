import time 

file = open("README.md", "r")

line = True
lines = file.readlines()

for line in lines:
    print(line.removesuffix("\n"))
    
    time.sleep(1)

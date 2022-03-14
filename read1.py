import time 

with open("README.md") as file:
    for line in file:
        print(line.removesuffix("\n"))
        time.sleep(1)

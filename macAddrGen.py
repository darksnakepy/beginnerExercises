import random


char_set = "ABCDEF0123456789"
mac_addr = ""
dot = 0

for _ in range(6):
    for _ in range(2):
        mac_addr += random.choice(char_set)
        if dot < 5:
          mac_addr += ":"
          dot += 1
            
print("mac address: ", mac_addr)
input()



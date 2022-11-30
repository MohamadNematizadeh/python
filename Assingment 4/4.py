print("welle")

i_list = [] 
inve_list = []  
print("!== break")

while True:
    num = input("--> ")
    if num == "!":
        break
    else:
        i_list.append(int(num))

for i in range(len(i_list)-1, -1, -1):
    inve_list.append(i_list[i])

print("Inverse List =", inve_list)
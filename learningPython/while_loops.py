lst = [2 , 3 , 3 ,-1]

i = 0

while i < len(lst):
    if lst[i] == -2:
        print("found the Number!!  ")
        break
    i += 1
else:
    print("Did'nt find the number! ")

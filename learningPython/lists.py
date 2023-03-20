x = [1,1,1,1,1,1,2,3,1,3.4,"Hello"]
'''
x.append("last element")
x.append(2) #method calling on a list.
x[0] ="h"
print(len(x))# function
s ="hello"

'''
popped = x.pop()
print(popped)
print(x)

count =x.count(1)
print(count)

index = x.index(1)
print(index)

remove = x.remove(1) # removes the 1st 
#occurance of number 1
print(x) 

list_contains_5 = 5 in x # post popular way to do
print(list_contains_5)

print(x[-1])
print(x[-9])
#print(x[-10])
# 
# Combine two lists
x=[1,2,3]
y = [1,2]
'''
combined = x +y
combined[0] = 100 
print(combined)
print(x)
print(y)

'''
x.extend([1,2])
y.extend(x)
print(x)
print(y)

lst = [[5,6,[100]],[2,3],[1,2,3]]
print(lst[0][-1][0])





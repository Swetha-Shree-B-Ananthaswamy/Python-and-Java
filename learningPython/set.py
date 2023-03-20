#x = {1,2,2,1,2,1, "hello" , 4 , True, 0.2 ,(1,2)}
#x.add(3)
#x.add(3)
#x.remove(2)
#contains = 4 in x
#print(contains)
#x.clear()
#print(len(x))

#x = {1,2}
#y = {2,3}

#z = x.union(y)
#print(z)

#m = x | y  # Union is pipe operator.
#print(m)

#p = {1,2,3}
#q = {1,2,4}
#s = p.intersection(q)
#print(s)
#s = p & q #& Intersection
#print(s)

#v ={1,2,3}
#b = {1,2,4}
#v.symmetric_difference_update(b)
#b.update(v)
#print(v)
#print(b)

#m = b - x
#print(b.difference(v)) # - is the shotcut
#print(m)
#print(b.symmetric_difference(v))
#print(v.symmetric_difference(b))
#print(v ^ b)

#k = {1,2,3}
#l = {1,2,3,4,5,6,7}

#print(k.issubset(l))
#print(k <= l)
#print(l >= k)
#print(l.issuperset(k))
#proper superset and proper subset
# k < l and l > k

#x = "hello"
#set_x = list(set(x))
#print(set_x)

numbers = set()
while True:
    num = int(input("Number: "))

    if num in numbers:
        break

    numbers.add(num)
    



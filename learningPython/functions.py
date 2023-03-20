#def print_value(value): #parameters
 #   print(value)

#def print_value():
#    print("hello")

#print_value("hello")
#print_value(1 )
#print_value(True)

#def get_negative_sum(x,y,z):
 #   result = x + y + z
  #  if result < 0:
   #     return result
   # return 1

#x = -4
#y = -5
#z = 100

#result = get_negative_sum( x , y ,z)
#print(result)

#range(1,10,2)#start , stop ,step

def new_range(start , stop=10 ):
    x =start
    while x < stop:
        print(x)
        x += 1

new_range(start =-5 ,stop =20)

def return_values(x,y):
    return x+1 ,y+1

x,y = return_values(3,5)
print(x,y)

def remove_chars(base , chars=""):
    new_strings = base
    for chr in chars:
        new_strings = new_strings.replace(chr ,"")
    return new_strings

results = remove_chars("hello word" ,"ol")
print(results)

def sum_lists(list1, list2):
    def sum_list(lst):
        total =0
        for num in lst:
             total += num
        return total
    list1sum = sum_list(list1)
    list2Sum = sum_list(list2)
    return list1sum , list2Sum

sum1 ,sum2 = sum_lists([1,2,3,4],[-1,-2,-3,-4])
print(sum1 ,sum2)













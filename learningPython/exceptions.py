
num = input("Enter an Number: ")

if not num.isdigit():
    raise ValueError("This is not a valid number! ")

print("Hello")
while True:
    num = input("Enter a valid number: ")
    try:
        num = float(num)
        break
    except ValueError as e:
        print("not a valid float , try again! ", e)



try:
    #2/0
    #int("hello")
    x ={}
    x[2] = 4

except Exception as e:
    print("Exception!", e)
finally:
    x =[1,2,3,4,5]
    print("Done!")        

#raise ValueError("This is an Error!")
#raise Exception("This is an Error")
#raise IndexError("This is an Error")




#int("hello")
#try:
    # 2/0
 #   int("hello")
#except ValueError as e:
 #   print("Exception!", e)
#except ZeroDivisionError as z:
 #   print("Exception " ,z)

#print("Done!")

    
    


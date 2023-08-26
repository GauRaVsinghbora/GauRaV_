#Question 3

x = int(input("Enter a integer: "))
y = int(input("Enter another integer: "))

if x >0 and y > 0 :
    if y % x == 0 : 
         print(x,"is divisible by", y)
    else:
         print(x," is not divisible", y)

else:
    print("invalid input")
    
    
    

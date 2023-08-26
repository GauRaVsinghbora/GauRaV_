#question4

num = int(input("Enter the 3 digit number: "))
x = num//100
y = num//10 % 10 
z = num % 10 
sum = x + y + z
print(sum)
if sum %3 ==0 :
    print("and sum of its digit is divisible by 3")
else :
    print("sum is not divisible by 3")




#question5 
num = int(input("Enter the 5 digit number: "))

x = str(num//10000)
y = str(num//1000 % 10)
z = str(num//100 % 10)
k = str(num// 10%10)
l = str(num % 10)

num3 = int(l+k+z+y+x )

print(l,k,z,y,x,sep = "")
if num == num3 :
    print("number is palindrome")
else:
    print("number is not palindrome")
print(type(num3))

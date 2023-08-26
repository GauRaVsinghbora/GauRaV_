#question2

s1= float (input("Enter the first side of triangle: "))
s2 = float(input(("Enter the second side of triangle: ")))
s3 = float(input( ("Enter the third side of triangle: ")))

if s1>0 and s2>0 and s3>0:
    if s1+s2>s3 or s2 +s3>s1 or s3+s1>s2:
    print("triangle is forming")
    else:
        print("error 404")
else:
    print("error 404")

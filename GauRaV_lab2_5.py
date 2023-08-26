radi = float(input("Enter the radius of circle: "))
unit = (input("type unit of radius(cm , m ): "))
if 1 < radi < 100:
    print(22/7*radi**2,unit,"^2")
else:
    print("out of range")
    


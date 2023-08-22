year = int(input("Enter year: "))

if year>0:
    if year % 4 == 0 :
        print(year,"is leap year")
    else:
        print(year,"is not leap year")
else:
    print("invalid input")
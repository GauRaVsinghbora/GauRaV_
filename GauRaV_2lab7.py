salary = int(input("Enter the salary: "))

if salary > 2500000:
    print("30% of the gross salary")
elif salary>1000000:
    print("20% of the gross salary")
elif salary>300000:
    print("10% of the gross salary")
else:
    print("0% of the gross salary")
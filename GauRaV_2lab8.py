salary =int (input("Enter your basic salary: "))
hra = salary * .20
ta = salary * .05
da = salary * .10

gross_salary = salary +hra + ta + da
print(gross_salary)

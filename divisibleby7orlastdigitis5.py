#WAP to check if the number is divisible by 7 or if the last digit is 5. 
n = int(input("Enter the number"))
if n%7==0 or n%10==5:
    print("Condition is satisfied")
else:
    print("Condition is not satisfied")    
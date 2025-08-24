#WAP to check if the number is divisible by 3 and the last digit is 4. 
n = int(input("Enter the number"))
if n%3==0 and n%10==4:
    print("The number is divisible by 3 and the last digit is 4")
else:
    print("Condition does not satisfy")    
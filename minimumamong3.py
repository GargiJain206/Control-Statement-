#Write a program to input three numbers(A, B & C) from the user and print the minimum element among A, B & C. 
A = int(input("Enter first number "))
B = int(input("Enter second number "))
C = int(input("Enter third number "))
minimum = min(A,B,C)
print("The minimum element is ",minimum)
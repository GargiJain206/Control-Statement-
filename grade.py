# Accept the percentage from the user and display the grade according to the following criteria. 
per = int(input("Enter a number "))
if per<25:
    print("Grade D")
elif 25<= per <=45:
    print("Grade C")   
elif 45< per <=65:
    print("Grade B")
elif 65< per <=85:
    print("Grade A")    
else:
    print("Grade A+")    



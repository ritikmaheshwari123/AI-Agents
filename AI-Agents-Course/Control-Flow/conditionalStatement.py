## if statement

age=20
if age>=18:
    print("You are an adult.")

## if-else statement
age=16
if age>=18:
    print("You are an adult.")
else:
    print("You are a minor.")   

## if-elif-else statement
marks=85            
if marks>=90:
    print("Grade: A")   
elif marks>=80:
    print("Grade: B")
elif marks>=70:
    print("Grade: C")
else:
    print("Grade: D")

## Nested if statement
num=15
if num>0:
    if num%2==0:
        print("The number is positive and even.")
    else:
        print("The number is positive and odd.")
else:
    print("The number is not positive.")

## Determine year is leap year
year=2020
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year.")    
else:
    print(f"{year} is not a leap year.")    



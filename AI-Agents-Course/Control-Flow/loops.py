## for loop

for i in range(5):
    print("Iteration:", i)  
print()
for i in range(2, 7):
    print("Iteration:", i)
print()
for i in range(1, 10, 2):
    print("Iteration:", i)  
print()
for i in range(10, 1, -1):
    print("Iteration:", i)  
print()

## string iteration
word = "Python"
for letter in word:
    print("Letter:", letter)    
print()

## while loop
count = 0
while count < 5:
    print("Count is:", count)
    count += 1
print()

## loop control statements
for i in range(10):
    if i == 3:
        print("Skipping 3")
        continue
    if i == 7:
        print("Breaking at 7")
        break
    print("Current number:", i)
print()

## pass statement
for i in range(5):
    if i % 2 == 0:
        pass  # Placeholder for future code
    else:
        print("Odd number:", i) 
print()

## nested loops
for i in range(3):
    for j in range(2):
        print(f"i: {i}, j: {j}")
print()


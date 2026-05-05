num = int(input("Enter a number to check: "))

if num > 50:
    print("The number is fortunately greater than 50.")
    if num%2==0:
        print("The number is even!")
    else:
        print("The number is odd!")
else:
    print("The number is unfortunately less than 50.")
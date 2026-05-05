s = "Shubham"
for i in s:
    print(i)
print("\n")

for i in range(1, 11,2):
    print(i)
print("\n")

n = int(input("Enter the number of rows: "))
for i in range(1, n+1):
    for j in range(i):
        print("*", end= '  ')
    print()
print("\n")

total_sum = 0
num = 1
while num <= 20:
    total_sum = total_sum + num
    num = num + 1
print(f"The sum of the first 20 positive integers is {total_sum}")
print("\n")

number = int(input("Enter a number: "))
if number > 1:
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            print(f"{number} is not a prime number.")
            break
        else:
            print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")
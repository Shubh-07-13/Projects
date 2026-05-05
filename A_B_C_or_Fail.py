a = int(input("What is your grade in Math? "))
b = int(input("What is your grade in English? "))
c = int(input("What is your grade in Science? "))
d = int(input("What is your grade in Social Studies? "))

g = (a+b+c+d)/4

if g <= 100:
    print("Your grade is an A. You are doing well.")
elif g <= 89:
    print("Your grade is a B.")
elif g <= 79:
    print("Your grade is a C.")
elif g <= 69:
    print("Your grade is a D. You have some work to do.")
elif 0 <= g <= 60:
    print("Your grade is failing, you have a LOT of work to do.")
else:
    print("You have a grade too interesting to be real.")

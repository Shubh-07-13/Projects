height = float(input("Enter your height in centimeters: "))
weight = float(input("Enter your weight in kilograms: "))
BMI = weight / (height/100)**2
print("Your BMI is", BMI)
if BMI <= 18.4:
    print("You are underweight.")
elif BMI <= 24.9:
    print("You are healthy.")
elif BMI <= 25.9:
    print("You are overweight. May want to go on a diet.")
elif BMI <= 29.9:
    print("You are very overweight. Consider going to the gym.")
elif BMI <= 34.9:
    print("It is what it is, you are obese. Gotta exercise!")
else:
    print("You are SEVERELY OBESE, you desperately NEED to go to the gym")
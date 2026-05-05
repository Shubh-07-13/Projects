workingdays = int(input("How many days are in the school year? "))
absentdays = int(input("How many days have you been absent from school? "))

realworkingdays = workingdays - absentdays

if realworkingdays < 0.75 * workingdays:
    print("You are not eligible to take the exam.")
else:
    print("You may take the exam.")
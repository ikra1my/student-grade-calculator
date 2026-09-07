# Student Grade Calculator

algorithm = float(input("Enter your Algorithm grade: "))
analysis = float(input("Enter your Analysis grade: "))
algebra = float(input("Enter your Algebra grade: "))

average = (algorithm + analysis + algebra) / 3

print("\nYour average is:", round(average, 2))

if average >= 10:
    print("Status: Passed ✅")
else:
    print("Status: Failed ❌")

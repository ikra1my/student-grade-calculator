# Student Grade Calculator

def get_grade(subject):
    while True:
        try:
            grade = float(input(f"Enter your {subject} grade (0-20): "))

            if 0 <= grade <= 20:
                return grade

            print("Please enter a grade between 0 and 20.")

        except ValueError:
            print("Please enter a valid number.")


algorithm = get_grade("Algorithm")
analysis = get_grade("Analysis")
algebra = get_grade("Algebra")

average = (
    algorithm * 5 +
    analysis * 4 +
    algebra * 2
) / 11

print("\n--- Results ---")
print("Weighted average:", round(average, 2))

if average >= 16:
    print("Mention: Excellent 🌟")
elif average >= 14:
    print("Mention: Very Good")
elif average >= 12:
    print("Mention: Good")
elif average >= 10:
    print("Mention: Pass")
else:
    print("Status: Failed ❌")

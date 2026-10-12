age = int(input("Enter your age: "))
if age >= 18:
    print("You are eligible for an airline ticket.")
elif age < 18:
    print("You are not eligible for an airline ticket.")
elif age >= 25:
    print("You are eligible for a senior citizen discount.")
else:
    print("Please you don't qualify for any ticket or discount.")    
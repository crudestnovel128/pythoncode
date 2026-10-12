# WEIGHT CONVERTER
weight = float(input("Enter weight(Kilograms or Grams): "))
unit = input("Enter unit (K for Kilograms, G for Grams): ")
if unit == "K" or unit == "k":
    weight_in_grams = weight * 1000
    unit = "Kilograms"
    print(f"{weight} Kilograms is equal to {weight_in_grams} Grams.")
elif unit == "G" or unit == "g":
    weight_in_kilograms = weight / 1000
    unit = "Grams"
    print(f"{weight} Grams is equal to {weight_in_kilograms} Kilograms.")
else:
    print("Invalid unit. Please enter 'K' for Kilograms or 'G' for Grams.")    
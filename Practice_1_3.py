# Practice three >>> Calculate bmi
w = float(input("Enter the weight in kilograms = "))
h = float(input("Enter the height in meters = "))

BMI = round(w / (h**2), 2)
print("BMI = ", BMI)
if BMI < 18.5:
    print("UNDERWEIGHT")
if 18.5 < BMI < 24.9:
    print("NORMAL")
if 25 < BMI < 29.9:
    print("OVERWEIGHT")
if 30 < BMI < 34.9:
    print("OBESE")
if BMI > 35:
    print("EXTREMELY OBESE")

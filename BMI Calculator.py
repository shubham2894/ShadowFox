height = float(input("Enter height in meters: "))
weight = float(input("Enter weight in kilograms: "))

if height > 0:
    bmi = weight / (height ** 2)
    print(f"BMI = {bmi:.2f}")

    if bmi >= 30:
        print("Obesity")
    elif 25 <= bmi < 30:
        print("Overweight")
    elif 18.5 <= bmi < 25:
        print("Normal")
    else:
        print("Underweight")
else:
    print("Height must be greater than zero!")

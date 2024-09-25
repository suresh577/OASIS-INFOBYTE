def calculate_bmi(weight, height_feet):
    height_meters = height_feet * 0.3048
    bmi = weight / (height_meters ** 2)
    return bmi

def main():
    print("Welcome to the BMI Calculator!")
    weight = float(input("Enter your weight in kilograms: "))
    height_feet = float(input("Enter your height (feet): "))
    bmi = calculate_bmi(weight, height_feet)
    print(f"Your BMI is: {bmi:.2f}")
    if bmi < 18.5:
        print("You are underweight.")
    elif 18.5 <= bmi < 24.9:
        print("You have a normal weight.")
    elif 25 <= bmi < 29.9:
        print("You are overweight.")
    else:
        print("You are obese.")

if __name__ == "__main__":
    main()

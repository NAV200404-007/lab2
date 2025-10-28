def calculate_bmi(height, weight):
 
    h = float(height)
    w = float(weight)

  
    bmi_value = w / (h * h)

    return bmi_value


def classify_bmi(bmi_value):
  

    if bmi_value < 18.5:
        return "Underweight"
    elif bmi_value < 25:
        return "Normal"
    elif bmi_value < 30:
        return "Overweight"
    else:
        return "Obese"


def main():
    print("BMI Calculator")

    height_input = input("Enter your height in meters (e.g. 1.75): ")
    weight_input = input("Enter your weight in kg (e.g. 68.5): ")


    print("Height = " + str(height_input))
    print("Weight = " + str(weight_input))


    bmi_value = calculate_bmi(height_input, weight_input)

    print("Your BMI is " + str(bmi_value))

    
    category = classify_bmi(bmi_value)
    print("BMI Category: " + category)



if __name__ == "__main__":
    main()

def calculate_bmi(height, weight):
    """
    Calculate Body Mass Index (BMI).

    height: height in meters (string or number)
    weight: weight in kilograms (string or number)

    returns: BMI as float
    """
    # Convert inputs to float so we can do math
    h = float(height)
    w = float(weight)

    # BMI formula:
    # BMI = weight(kg) / (height(m) * height(m))
    bmi_value = w / (h * h)

    return bmi_value


def classify_bmi(bmi_value):
    """
    Classify BMI into ranges.
    These ranges are the common WHO-style cutoffs.
    """

    if bmi_value < 18.5:
        return "Underweight"
    elif bmi_value < 25:
        return "Normal"
    elif bmi_value < 30:
        return "Overweight"
    else:
        return "Obese"


def main():
    print("BMI Calculator v2")

    # Ask the user for inputs as strings (console input)
    height_input = input("Enter your height in meters (e.g. 1.75): ")
    weight_input = input("Enter your weight in kg (e.g. 68.5): ")

    # Show what was entered (the lab shows printing the values) :contentReference[oaicite:2]{index=2}
    print("Height = " + str(height_input))
    print("Weight = " + str(weight_input))

    # Compute BMI
    bmi_value = calculate_bmi(height_input, weight_input)

    # Print BMI (converted to string using str(), which fixes the type error when concatenating) :contentReference[oaicite:3]{index=3}
    print("Your BMI is " + str(bmi_value))

    # Classify BMI range (the lab says to display a BMI classification using a table of BMI ranges). :contentReference[oaicite:4]{index=4}
    category = classify_bmi(bmi_value)
    print("BMI Category: " + category)


# Standard Python entry point pattern the lab talks about:
if __name__ == "__main__":
    main()

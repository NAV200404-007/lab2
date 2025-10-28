def calculate_bmi(height, weight):

    height = float(height)
    weight = float(weight)

    print("Height = " + str(height))
    print("Weight = " + str(weight))

    bmi= weight/(height*height)
    print("bmi = " ,bmi)

    if bmi < 18.5:
        return "Underweight"
    elif bmi <25:
        return "Normalweight"
    elif bmi <30:
        return "Overweight"
    else:
        return "obese"



result = calculate_bmi(weight="57", height="1.73")
print("BMI Category:", result)
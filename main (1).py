# BMI finder
# Created by: Umair
# Created on: Oct 21, 2021
# Program will ask the user to input age, height and weight and output their BMI description

# Asks the user to input the age and stores it in a variable
age = input("Enter your age: ")

bmi = ""  # Variable holder

# Checks if input age is greater than or equal to 18 and then proceeds to calculate the BMI.
if (age >= "18"):

    # Asks user what units they would like to use and stores it in a variable
    units = input("What units would you like to use? Metric (M) or Imperial (I)? ")

    # Converts the units input to lowercase and checks to see if user wants to use metric
    if ("metric" in units.lower() or "m" in units.lower()):

        #Asks the user to input weight and height and stores them in a variable
        weightM = input("\nEnter your weight in kilograms: ")
        heightM = input("Enter your height in centimeters: ")

        #Converts weight and height into imperial measurements to calculate BMI later
        weightM = int(weightM) * 2.205
        heightM = int(heightM) / 2.54

        # Sets the weight and height to type float before calculating.
        bmi = ((float(weightM) * 703) / (float(heightM)**2))
        #print the BMI result rounded to 1 decimal point by using the round() function.
        print("\nYour BMI is", round(bmi, 1))

        # Checks to see if bmi is lower than 15, if True prints "Very severely underweight"
        if bmi < 15:
            print("Very severely underweight")
        # Checks to see if bmi is greater than 15 and less than 16, if True prints "Severely underweight"
        elif bmi >= 15.0 and bmi < 16.0:
            print("Severely underweight")
        # Checks to see if bmi is greater than or equal to 16 and less than 18.5, if True prints "Underweight"
        elif bmi >= 16 and bmi < 18.5:
            print("Underweight")
        # Checks to see if bmi is greater than or equal to 18.5 and less than 25, if True prints "Normal"
        elif bmi >= 18.5 and bmi < 25:
            print("Normal")
        # Checks to see if bmi is greater than or equal to 25 and less than 30, if True prints "Overweight"
        elif bmi >= 25 and bmi < 30:
            print("Overweight")
        # Checks to see if bmi is greater than or equal to 30 and if bmi less than 35, if True prints "Severely overweight"
        elif bmi >= 30 and bmi < 35:
            print("Severely overweight")
        # Checks to see if bmi is greater than or equal to 35, if True prints "Very severely overweight"
        elif bmi >= 35:
            print("Very severely overweight")

    # Converts the units input to lowercase and checks to see if user wants to use imperial
    elif ("inperial" in units.lower() or "i" in units.lower()):

        # Asks the user to input the weight in pounds and stores it in a variable
        weight = input("\nEnter your weight in pounds: ")

        # Asks the user to input the height in inches and stores it in a variable
        height = input("Enter your height in inches: ")

        # Sets the weight and height to type float before calculating.
        bmi = ((float(weight) * 703) / (float(height)**2))
        #print the BMI result rounded to 1 decimal point by using the round() function.
        print("\nYour BMI is", round(bmi, 1))

        # Checks to see if bmi is lower than 15, if True prints "Very severely underweight"
        if bmi < 15:
            print("Very severely underweight")
            # Checks to see if bmi is greater than 15 and less than 16, if True prints "Severely underweight"
        elif bmi >= 15.0 and bmi < 16.0:
            print("Severely underweight")
            # Checks to see if bmi is greater than or equal to 16 and less than 18.5, if True prints "Underweight"
        elif bmi >= 16 and bmi < 18.5:
            print("Underweight")
            # Checks to see if bmi is greater than or equal to 18.5 and less than 25, if True prints "Normal"
        elif bmi >= 18.5 and bmi < 25:
            print("Normal")
        # Checks to see if bmi is greater than or equal to 25 and less than 30, if True prints "Overweight"
        elif bmi >= 25 and bmi < 30:
            print("Overweight")
            # Checks to see if bmi is greater than or equal to 30 and if bmi less than 35, if True prints "Severely overweight"
        elif bmi >= 30 and bmi < 35:
            print("Severely overweight")
            # Checks to see if bmi is greater than or equal to 35, if True prints "Very severely overweight"
        elif bmi >= 35:
            print("Very severely overweight")
# Else statement, runs if age is less than 18
else:
    print("\nInvalid age. Please enter an age 18 or over.")

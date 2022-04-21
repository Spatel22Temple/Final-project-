#Shivampatel
#macr0s



import time
 
print("Starting app, Please wait.")
time.sleep(7)
print("Loading complete.")




print ("Welcome to Macr0s")
print ("An app that will help you lose weight and understand your macros")

print ("WARNING: Macr0s may or may not be 100% accurate.")



    
                

def bmr_calc():
        
    
    Pounds = int(input("Enter your weight: "))
    Inch= int(input("Enter your height in inches: "))
    age = int(input("Enter your age: "))
    gender = input(" Are you a male or female?").lower()

    Metric = Pounds / 2.2
    Centi = Inch * 2.54
    bmr=None
    if gender =="male":
        bmr = int((10 * Metric) + (6.25 * Centi) - (5 * age) + 5)
    elif gender == "female":
        bmr = int ((10 * Metric) + (6.25 * Centi) - (5 * age) - 161)
    print ("your metabolic rate is " + str(bmr) + ",")

  
            
    return bmr




def calories_needs (bmr):
    print(
    "1 = inactive \n2 = exercise 1 -3 times a week \n3 = exercise 4 -5 times a week\n4 = daily exercise or intense exercise 3-4 times a week\n5 = intense exercise 6 times a wekk")
    Physical  = int(input( "select your activity level: "))
    PhysicalIndex = 0
    if Physical  == 1:
            PhysicalIndex = 1.2
    elif Physical  == 2:
            PhysicalIndex = 1.375
    elif Physical  == 3:
            PhysicalIndex = 1.46
    elif Physical  == 4:
            PhysicalIndex = 1.725
    elif Physical  == 5:
            PhysicalIndex = 1.9
    CaloriesNeeded = int( bmr * PhysicalIndex)
    print("to maintain your current weight you need" + str(CaloriesNeeded) + " calories a day.")
    return CaloriesNeeded


def calculateMacros(calories):

    CP = int(.4* calories)
    caloriesInprotein = int(CP / 4)
    caloriesFromcarbs = int(.4 * calories)
    calsCarbs = int(caloriesFromcarbs /4)
    calsFromfat = int(.2 * calories)
    calsInfat = int(calsFromfat / 9)

    print("calories from Protein " + str(CP) + " / " + str(caloriesInprotein) + " grams of protein")
    print("calories from carbs: " + str(caloriesFromcarbs) + " / " + str(calsCarbs) + " grams of carbs.")
    print("calories from fat: " + str(calsFromfat) + " / " + str(calsInfat) + " grams of fat.")
    print ("/n")

    halfPoundWeek_calories = int(calories - int((3500 / 2) / 7))
    print("to lose .5 of a pound a week, you need to eat" + str(halfPoundWeek_calories) + "calories a day")
    
    CP = int(.4 * halfPoundWeek_calories)
    caloriesInprotein = int(CP / 4)
    caloriesFromcarbs = int(.4 * halfPoundWeek_calories)
    calsCarbs = int(caloriesFromcarbs / 4)
    calsFromfat = int(.2 * halfPoundWeek_calories)
    calsInfat = int(calsFromfat / 9)

    print("calories from protein: " + str(CP) + " / " + str(caloriesInprotein) + "grams of protein. ") 
    print("calories from Carbs " + str(caloriesFromcarbs) + " / " + str(calsCarbs) + " grams of carbs.")
    print("calories from fat:" + str(calsFromfat) + " / " + str(calsInfat) + " grams of fat.")
    print("\n")


    print ("Thank you for using Macr0s, good luck on your weight loss journey.")



                                            




bmr = bmr_calc()
CaloriesNeeded =calories_needs(bmr)
calculateMacros(CaloriesNeeded)
                                         

    
        



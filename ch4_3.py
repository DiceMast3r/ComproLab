def calculateBMI(height, weight):
    # put your code below
    height = float(height)
    weight = float(weight)
    bmi = weight / ((height / 100)**2)
    return bmi
    
def getInput():
    # put your code below
    get = input("Enter height(cm) weight(kg) : ")
    return get
    
def bmiConclusion(bmi):    
    # put your code below
    if bmi < 18.5:
        return "You're underweight."
    elif bmi < 25:
        return "You're normal."
    elif bmi < 30:
        return "You're overweight."
    elif bmi < 35:
        return "You're obese."
    else:
        return "You're extremly obese."
    
print(" *** BMI Calculation ***")
height, weight = getInput().split()
bmi = calculateBMI(height, weight)
print("Your BMI is %.2f" %bmi)
print(bmiConclusion(bmi))

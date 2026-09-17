def bmi_calculator(weight,height):
    bmi=weight/((height/100)**2)
    return round(bmi,2)

def bmr_calculator(gender,age,weight,height):
    if gender=="male":
        bmr=(10*weight)+(6.25*height)-(5*age)+5
        return bmr

    elif gender=="female":
        bmr=(10*weight)+(6.25*height)-(5*age)-161
        return bmr

def tdee_calculator(bmr,activity):
    activity_factor={
        "Sedentary":1.20,
        "Lightly Active":1.375,
        "Modrately Active":1.55,
        "Very Active":1.725,
        "Extra Active":1.90
    }

    tdee=bmr*activity_factor[activity]
    return round(tdee,2)

def calorie_target(tdee,aim):
    if aim == "weight maintain":
        calorie=tdee
    elif aim == "weight loss":
        calorie=tdee-400
    elif aim == "weight gain":
        calorie=tdee+300
    return round(calorie,2)


# Testing These Functions working properly or not?
# print(bmi_calculator(60,150))
# bmr=bmr_calculator("male",25,50,150)
# print(tdee_calculator(bmr,"Very Active"))
# tdee=tdee_calculator(bmr,"Very Active")
# print(calorie_target(tdee,"weight loss"))
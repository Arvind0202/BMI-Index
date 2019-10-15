'''BMI Calculator using Exceptional handling to validate Input entry'''

def read_value():
    "Returns the users weight and height"
    while True:
        try:
            weight=float(input("Enter the weight in Kg"))
            height=float(input("Enter the height in meter"))
            break
        except ValueError:
            print("Invalid entry reenter the values....")
    return weight,height
        
def cal_bmi(weight,height):
    "Calculates the BMI"    
    bmi=round(weight/(height*height),2)
    print("BMI",bmi)
    return bmi

def check_bmi(weight,height):
    "Check the category"
    bmicheck=cal_bmi(weight,height)
    if bmicheck<=18.5:
        print("under weight")
    elif bmicheck>18.5 and bmicheck<=24.9:
        print("normal weight")
    elif bmicheck>=25 and bmicheck<=29.9:
        print("over weight")
    else:
        print("Obese")

#----START OF SCRIPT
if __name__=='__main__':
    users_weight,users_height = read_value()
    check_bmi(users_weight,users_height)
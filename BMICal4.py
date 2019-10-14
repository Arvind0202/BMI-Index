'''BMI Calculator using Exceptional handling to validate Input entry'''

weight=height=1
def read_value():
    global weight,height,bmicheck
    while True:
        try:
            weight=float(input("Enter the weight in Kg"))
            height=float(input("Enter the height in meter"))
            break
        except ValueError:
            print("Invalid entry reenter the values....")
        
def cal_bmi():    
    bmi=round(weight/(height*height),2)
    print("BMI",bmi)
    return bmi
def check_bmi():
    bmicheck=cal_bmi()
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
    read_value()
    check_bmi()
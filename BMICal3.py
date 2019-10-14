"""
We will use this script to teach Python to absolute beginners
The script is an example of BMI implemented in Python

The BMI Calculator using IF ELse
    Less than or equal to 18.5 is represents underweight
    Between 18.5 -24.9 indicate normal weight
    Between 25 -29.9 denotes overweight
    Greater than 30 denotes obese

Functions:

Create a function to get the input
Create one more function to calculate BMI
Create one more function for checking user category
"""
weight=height=1
def read_value():
    global weight,height
    weight=float(input("Enter the weight in Kg"))
    height=float(input("Enter the height in meter"))
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

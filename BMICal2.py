"""
We will use this script to teach Python to absolute beginners
The script is an example of BMI implemented in Python

The BMI Calculator using IF ELse
    Less than or equal to 18.5 is represents underweight
    Between 18.5 -24.9 indicate normal weight
    Between 25 -29.9 denotes overweight
    Greater than 30 denotes obese
"""
def bmi():
    "This method implements bmi"
    weight=int(input("Enter teh weight in Kg"))
    height=int(input("Enter the height in meter"))
    bmi=weight/(height*height)
    print("BMI",bmi)
    if bmi<=18.5:
        print("under weight")
    elif bmi>18.5 and bmi<=24.9:
        print("normal weight")
    elif bmi>=25 and bmi<=29.9:
        print("over weight")
    else:
        print("Obese")

#----START OF SCRIPT
if __name__=='__main__':
    bmi()

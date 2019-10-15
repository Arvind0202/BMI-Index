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
    weight=int(input("Enter the weight in Kg"))
    height=int(input("Enter the height in meter"))
    userbmi=weight/(height*height)
    print("BMI of the user is ",userbmi)
    if userbmi<=18.5:
        print("under weight")
    elif userbmi>18.5 and userbmi<=24.9:
        print("normal weight")
    elif userbmi>=25 and userbmi<=29.9:
        print("over weight")
    else:
        print("Obese")

#----START OF SCRIPT
if __name__=='__main__':
    bmi() 

''' BMI Calculator
Create a function to get the input
Create a function to calculate BMI
Create one more function for checking user category
Create a function to read the CSV file and return the matched player'''


import csv
weight=height=1
def read_value():
    # exception handling. The tallest man is 2.72 m
    while True:
        try: 
            weight=float(input("Enter the weight in Kg"))
            height=float(input("Enter the height in meter"))
            if 0 < weight < 150 and 0 < height < 2.72:
                print("BMI CALCULATION....")
            else:
                raise ValueError
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

def read_file():
    count=0
    nodata=0
    bmicheck=str(cal_bmi())
    with open('c:/Users/vino/code/BMI-Index/all_players_data.csv','r')as f:
        data = csv.reader(f)
        for row in data:
            count=count+1
            if(row[3]==bmicheck):
                print(row)
                flag=1
            else:
                flag=0
                nodata=nodata+1
    if(flag==0 and nodata==count):
        print('no matching data')


#----START OF SCRIPT
if __name__=='__main__':
    "Main program here"
    read_value()
    check_bmi()
    read_file()

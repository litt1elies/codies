#2024 nov 16
height=float(input("enter your height (cm)"))
print("")
weight=float(input("enter your weight (kg)"))
print("")
print("")
if height>= 182.88 :
    feet=6
    c=182.88
elif height>= 152.4 :
    feet=5
    c=152.4
elif height>= 121.92:
    feet=4
    c=121.92
elif height>= 91.44:
    feet=3 
    c=91.44
elif height>= 60.96:
    feet=2
    c=60.96
elif height>= 30.48:
    feet=1
    c=30.48

he=height-c

if he>= 27.49 :
    inch=11
elif he>= 25.4 :
    inch=10
elif he>= 22.86:
    inch=9
elif he>= 20.32:
    inch=8
elif he>= 17.78:
    inch=7
elif he>= 15.25:
    inch=6
elif he>= 12.7 :
    inch=5
elif he>= 10.16:
    inch=4
elif he>= 7.62:
    inch=3
elif he>= 5.08:
    inch=2
elif he>= 2.54:
    inch=1
elif he>= 0:
    inch=0
    
print("your height is",feet,"'",~int(inch))
print("")
met=height/100
wei=int(weight*2.205)
print("your weight in pounds is",wei)
bmi=float(weight / (met*met))
print("")
print("your BMI is",(bmi))
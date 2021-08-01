# BMI Calculator
Name=input("Enter your name")
height_cm= float(input("Your height in cm: "))
weight_kg=int(input("Your weight in KG :"))

BMI = weight_kg /(height_cm /100)**2 
print(' ')
print("BMI : ",BMI)
print(' ')
print(Name)

if BMI <= 18.4:
     print("You are underweight.")
elif BMI <= 24.9:
     print("Hurray! You are healthy.")
elif BMI <= 29.9:
    print("You are over weight. \nIts not late yet proper exercise and diet will help you to become healthy.")
elif BMI <= 34.9:    
    print("You are severely over weight.  \nYou need to work on your Diet and Exercise. Start from today")
elif BMI <= 39.9:
    print("You are obese. \nYou need to consult doctor and work on your Diet and Exercise Immediately.")
else:
    print("You are severely obese, \nYou need to consult doctor and work on your Diet and Exercise Immediately.")

Bye=input(" Hit enter to exit, Thank You!")

hcm = int(input("What's your height?")) #height in cm
m = float(input("How much do you weigh?"))

h = hcm / 100 #convert to m

BMI = m / (h * h)

if BMI < 16:
    print("Severly underweight")
elif 16 < BMI < 18.5 :
    print("Underweight")
elif 18.5 < BMI < 25 :
    print("Normal")
elif 25 < BMI < 30 :
    print ("Overweight")
else:
    print ("Obese")
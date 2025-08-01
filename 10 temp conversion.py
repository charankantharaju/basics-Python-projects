unit = input ("is the temp is in celcius or fahreheit (C/F): ")
temp= float(input("enter the temp"))

if unit == "C":
    temp = round((9*temp)/5 +32,1) #formula
    print(f"the temp im fahrenheit is : {temp}F")
elif unit == "F":
    temp = round((temp-32)*5/9,1) #formula
    print(f"the temp im fahrenheit is : {temp}C")
else :
    print(f"{unit} is a invalid unit")
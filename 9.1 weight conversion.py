weight= float(input("enter your weight : "))
unit = input(" enter the weigt in (K/P)")  # k=kg , p=pounds 
if unit == "K":
    weight = weight *2.205
    unit="lbs"
elif unit == "P":
    weight = weight /2.205
    unit="kgs"
else :
    print(f"{unit} was not valid  ")
print(f"your weight is {round(weight,1)} {unit}")
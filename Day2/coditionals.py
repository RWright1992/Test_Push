age = int(input("Gis yer age: "))
if age >= 85:
    print("85 or older")
elif age >= 100:
    print("This will never trigger")
elif age >= 65:
    print("Between 65 and 85")
elif age >= 45:
    print("Between 45 and 65")
else:
    print("Young")

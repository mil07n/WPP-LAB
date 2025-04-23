#Take length input in feet
#give option to convert feet into other:
# 1- inches
# 2- yards
# 3- miles
# 4- millimeters
# 5- centimeters
# 6- meters
# 7- kilometers
length=float(input('Length in Feet: '))
option=int(input('Enter desired conversion\n[1] - Feet to Inches\n[2] - Feet to Yards\n[3] - Feet to centimeters\n'))
conversion=[12,1/3,5280]
conversionname=["inches","yards","centimeters"]
print(f"{length} feet = {conversion[option-1]*length} {conversionname[option-1]}")
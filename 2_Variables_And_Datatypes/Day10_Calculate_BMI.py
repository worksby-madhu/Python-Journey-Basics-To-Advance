w = int(input("Enter WEIGHT in Kgs: ")) #43
h = float(input("Enter height in meters: ")) #1.58
bmi = w // (h ** 2) 
"""Floor division"""
print("ur BMI is:",bmi) #17.0
bmi = w / (h ** 2) 
"""normal division"""
print("ur BMI is:",bmi) #17.224803717352987
print("ur BMI is:",round(bmi)) #17
"""round() function is used to make numbers shorter and cleaner by limiting decimal places"""
print("ur BMI is:",round(bmi,5)) #17.2248
"""round(number, digits) here limiting to 5"""
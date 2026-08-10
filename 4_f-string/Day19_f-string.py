name="Subhadra"
age=21
cgpa = 8.6
print(f"My name is {name}") #My name is Subhadra
print(f"My age is {age}. My brothers age is {age+2}") #My age is 21. My brothers age is 23

fruits = ["Apple", "Mango", "Orange"]
print(f"My favorite fruit is {fruits[1]}") #My favorite fruit is Mango

student = {
    "name": "Subhadra",
    "marks": 95
}
print(f"{student['name']} scored {student['marks']} marks") #Subhadra scored 95 marks

print(f"Student Name : {name}") #Student Name : Subhadra
print(f"Age          : {age}")
print(f"CGPA         : {cgpa:.2f}")
print(f"Next Year Age: {age + 1}")
print(f"Eligible to Vote? {age >= 18}")



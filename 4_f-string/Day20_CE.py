age=int(input("Enter your current age:"))
years_left=90-age
a=365*years_left
b=52*years_left
c=12*years_left
#print("You have",a,"days,",b,'weeks and',c,'months left.' )
print(f"You have {a} days, {b} weeks and {c} months left.")
# Using f-strings instead of regular print statements with commas
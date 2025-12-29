birthYear = input('Birth year: ')
print(type(birthYear))

# Convert / pars birthYear into int instead of str
age = 2025 - int(birthYear)

print(type(age))
print(age)

# exercise 
weight_lbs = input("What is your weight? ")
weight_kilo = 0.45359237 * float(weight_lbs)
print("Weight in pounds: " + str(weight_lbs)  + " lbs " + "\nWeight in kilograms: " + str(weight_kilo) + " kg ")
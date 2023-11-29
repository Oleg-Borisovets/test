massa = int(input("Ввидте свой вес"))
rost = int(input("Ввидите свой рост"))

BMI  = int(massa / rost**2 * 10000)
print(BMI)
a = "="
print("20", a*(BMI - 21), "|", a*(49 - BMI), "50")

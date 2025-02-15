# Scaning age of Cliemt to get his price
client_age = int(input("Enter your age: "))

if client_age < 5:
    print("The ticet is free!!!")
elif client_age >=5 and client_age < 10:
    print("The ticket price is 5.0 $")
elif client_age >=10 and client_age < 18:
    print("The ticket price is 6.0 $")
elif client_age >= 18 and client_age < 27:
    print("The ticket price is 7.0 $")
else:
    print("The ticket price is 10.0 $")
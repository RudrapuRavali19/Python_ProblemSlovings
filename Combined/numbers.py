num = int(input("Enter a number: "))

if num % 2 == 0 and num % 5 == 0:
    print("Divisible by both 2 and 5")
elif num % 2 == 0:
    print("Divisible by 2")
elif num % 5 == 0:
    print("Divisible by 5")
else:
    print("Neither divisible by 2 nor 5")
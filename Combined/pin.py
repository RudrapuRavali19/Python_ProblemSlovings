correct_pin = "1234"
attempts = 3

while attempts > 0:
    pin = input("Enter 4-digit PIN: ")
    if pin == correct_pin:
        print("Access Granted")
        break
    else:
        attempts -= 1
        print(f"Wrong PIN. {attempts} attempts left")
else:
    print("Card Blocked")
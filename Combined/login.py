correct_pass = "1234"
attempts = 3

while attempts > 0:
    password = input("Enter password: ")
    if password == correct_pass:
        print("Login Successful")
        break
    else:
        attempts -= 1
        print(f"Wrong password. {attempts} attempts left")
else:
    print("Account Locked")
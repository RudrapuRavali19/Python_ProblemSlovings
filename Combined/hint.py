secret = 42 # you can change this
guess = -1

while guess!= secret:
    guess = int(input("Guess the number: "))
    
    if guess == secret:
        print("Correct! You guessed it")
    elif guess > secret + 10:
        print("Very High")
    elif guess > secret:
        print("High")
    elif guess < secret - 10:
        print("Very Low")
    else:
        print("Low")
    
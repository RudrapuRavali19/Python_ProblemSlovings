num = int(input("Enter a number: "))

sum_digits = 0
temp = num
while temp > 0:
    sum_digits += temp % 10
    temp //= 10

if sum_digits % 7 == 0:
    print("Lucky Number")
else:
    print("Not Lucky Number")
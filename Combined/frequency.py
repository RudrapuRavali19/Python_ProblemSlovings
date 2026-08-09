num = input("Enter an integer: ")
digit = input("Enter digit to count: ")

count = 0
i = 0
while i < len(num):
    if num[i] == digit:
        count += 1
    i += 1
print(f"Digit {digit} appears {count} times")
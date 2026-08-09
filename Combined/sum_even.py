N = int(input("Enter N: "))

sum_even = 0
for i in range(2, N + 1, 2):
    sum_even += i
print("Sum of even numbers:", sum_even)
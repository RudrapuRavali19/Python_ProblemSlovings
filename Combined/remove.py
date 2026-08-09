s = input("Enter string with letters and digits: ")

result = ""
for ch in s:
    if not ch.isdigit():
        result += ch
print("String without digits:", result)
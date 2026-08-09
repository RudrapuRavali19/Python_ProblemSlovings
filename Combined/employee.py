emp_id = input("Enter Employee ID: ")

if len(emp_id) == 8 and emp_id.startswith("EMP") and emp_id[3:5].isalnum() and emp_id[5:].isdigit():
    print("Valid Employee ID")
else:
    print("Invalid Employee ID")
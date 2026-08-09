attendance = input("Enter 7 days attendance as P/A: ").upper()

present = attendance.count('P')
absent = attendance.count('A')
total_days = 7
percentage = (present / total_days) * 100

print("Total Present:", present)
print("Total Absent:", absent)
print("Attendance %:", percentage)

if percentage < 75:
    print("Attendance is below 75%")
else:
    print("Attendance is good")
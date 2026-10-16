student = {
    "name": "Shiv",
    "age": 22,
    "course": "BCA"
}

key = input("Enter key to update: ")

if key in student:
    value = input("Enter new value: ")
    student[key] = value
    print("Updated Dictionary:", student)
else:
    print("Key not found")
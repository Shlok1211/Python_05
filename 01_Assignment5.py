studentInfo = {
    'Rohan': 90,
    'Ali': 95,
    'Naman': 89,
    'Ram': 99,
    'Alice': 85
}

userInput = input("Enter the students's name: ")
if userInput in studentInfo:
    print(f"{userInput}'s marks: {studentInfo[userInput]}")
else:
    print('Student not found.')

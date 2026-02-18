Set Basics

numbers = {10, 20, 30, 20, 40}

print("Set:", numbers)

print("Length:", len(numbers))

numbers.add(50)
print(numbers)

numbers.remove(20)
print(numbers)

print("Check 30 in set:", 30 in numbers)

# Loop
print("Looping elements:")
for n in numbers:
    print(n)

Dictionary Basics

student = {
    "name": "Pooja",
    "age": 21,
    "course": "Python"
}

print("Dictionary:", student)

print("Name:", student["name"])

student["age"] = 22
print("Updated age:", student)

student["city"] = "Chennai"
print("After adding city:", student)

print("Keys:", student.keys())

print("Values:", student.values())

# Loop
print("Looping dictionary:")
for key, value in student.items():
    print(key, ":", value)

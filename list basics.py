


numbers = [5, 10, 15, 20, 25]

print("List:", numbers)

print("Length:", len(numbers))

print("First:", numbers[0])

numbers.append(30)
print(numbers)

numbers.remove(10)
print(numbers)

print("Even numbers:")
for n in numbers:
    if n % 2 == 0:
        print(n)

print("Sum:", sum(numbers))

print("Max:", max(numbers))

print("Min:", min(numbers))

print("Reversed:", numbers[::-1])

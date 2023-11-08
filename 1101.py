with open('1101-1\one_hundred.txt', 'r') as file:
    numbers = file.read().split()
numbers = [int(num) for num in numbers if num.isdigit()]
missing_numbers = [num for num in range(1, 100) if num not in numbers]
print(F"The missing numbers are {missing_numbers}")
numbers.sort()
with open("one_hundred_sorted.txt", "w") as file:
    for num in numbers:
        file.write(str(num) + "\n")


count = int(input("Enter the count of numbers: "))

total = 0

for i in range(count):
    num = int(input("Enter an integer: "))
    total += num

average = total / count
print("The average is:", average)


total = 0
count = 0
while count < 10:
    try:
        num = float(input("Enter a real number: "))
        total += num
        count += 1
    except ValueError:
        print("Invalid input. Please enter a real number.")

average = total / 10
print("Average is:", average)

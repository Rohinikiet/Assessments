
def check_even(a):
    if a % 2 == 0:
        return "the number is even"
    else:
        return "the number is odd"
a = int(input("enter the number:"))
result = check_even(a)
print(result)

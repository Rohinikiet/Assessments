
input1 = input("Enter the first string: ")
input2 = input("Enter the second string: ")

input1 = input1.replace(" ", "").lower()
input2 = input2.replace(" ", "").lower()

if sorted(input1) == sorted(input2):
    print("Strings are anagrams.")
else:
    print("Strings are not anagrams.")

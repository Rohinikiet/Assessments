#check strings are anagrams or not
input1 = input("Enter the first string: ")
input2 = input("Enter the second string: ")

input1 =input1.lower()
input2 = input2.lower()

if sorted(input1) == sorted(input2):
    print("Strings are anagrams.")
else:
    print("Strings are not anagrams.")

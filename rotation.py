print("Enter the first string:")
str1=input()
print("Enter the second string:")
str2=input()

is_rotation = False

if len(str1) == len(str2):
    temp= str1 + str1
    if str2 in temp:
        is_rotation = True
if is_rotation:
    print(f"'{str2}' is a rotation of '{str2}'.")
else:
    print(f"'{str2}' is not a rotation of '{str1}'")

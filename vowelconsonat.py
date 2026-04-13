Vowels_count = 0
Consonants_count = 0
vowels = "aeiou"

input_string=input("Enter a string:").lower()

for char in input_string:
    if 'a'<=char<='z':
        if char in vowels:
            Vowels_count+=1
        else:
            Consonants_count+=1
print(f"Vowels:{Vowels_count}")
print(f"Consonants:{Consonants_count}")

string=input("Enter a string:")
len=len(string)
print("All substring:")
for i in range(len):
    for j in range(i,len):
        substring=string[i:j+1]
        print(substring)

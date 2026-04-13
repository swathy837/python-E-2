s=input("Enter a string:")
result=""
for i in range(0,len(s),2):
    char=s[i]
    n=int(s[i+1])
    result+=char*n
print("Output string:",result)

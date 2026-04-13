s=input("Enter the string:")
l=len(s)
if l>=3:
    if s.endswith("ing"):
       print("ans:",s+"ly")
    else:
       print("ans:",s+"ing")
else:
    print(s)

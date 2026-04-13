p=input("Enter your password:")
if((8<=len(p)<=15)and
    any(ch.islower() for ch in p)and
    any(ch.isupper() for ch in p)and
    any(not ch.isalum() for ch in p)and
    not any(ch.isspace() for ch in p)):
    print("Valid password")
else:
    print("Invalid password")

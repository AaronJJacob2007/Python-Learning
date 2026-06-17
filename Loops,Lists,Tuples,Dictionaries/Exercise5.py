#name>3 char  and name< 50 char
name=input("Enter name ")
if len(name)<3:
    print("Name must be atleast 3 characters long")
elif len(name)>50:
    print("Max length is 50 chars")
else:
    print("Name looks good!")

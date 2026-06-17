conv={
    "1":"One",
    "2":"Two",
    "3":"Three",
    "4":"Four",
    "5":"Five",
    "6":"Six",
    "7":"Seven",
    "8":"Eight",
   " 9":"Nine"
}
val=input("Enter Phone Number")
output=""
for item in val:
    output+=conv.get(item,"!")+" "
print(output)
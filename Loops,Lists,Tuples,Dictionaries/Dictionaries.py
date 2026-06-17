customer={
         "name":"Aaron",
         "age":19,
         "is_verified":True

}
print(customer["name"])
print(customer.get("Name"))
print(customer.get("Birthdate","May 29 2007"))
customer["name"]="Jack Smith"
print(customer["name"])
customer["bday"]="May 29 2007"
print(customer["bday"])

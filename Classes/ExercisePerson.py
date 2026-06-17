class Person:
    def __init__(self,name):
        self.name=name

    def talk(self):
        print(f"Hi,I am {self.name}")

p=Person("Aaron Jacob")
print(p.name)
p.talk()

p2=Person("Bob")
p2.talk()

class Employee(Person):
    pass

emp=Employee("Aaron Jacob")
emp.talk()


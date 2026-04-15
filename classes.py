class Person:
    def __init__(self,name,age,address,email):
        self.name = name
        self.age = age
        self.address = address
        self.email = email

    def talks(self):
        print(f"{self.name} talks")

    def walks(self):
        print(f"{self.name} is walking")

        
#person1 object      
person1 = Person("Mike",24,'Karen','mike@mail.com')
print(type(person1))
print(person1.address)
person1.talks()
person1.walks()


#person2 object
person2 = Person("Kate",21,'Eastleigh','kate@mail.com')
print(type(person2))
print(person2.name)
person2.talks()
person2.walks()





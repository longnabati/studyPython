class Student:
    def __init__(self, name, age, address):
        self.age = age
        self.name = name
        self.address = address
        
    def show_info(self):
        print(f'''STUDENT INFO
Name    : {self.name}
Age     : {self.age}
Address : {self.address}
              
              ''')
    #dunder method
    def __str__(self):
        return f"<Student (name = {self.name}, age = {self.age})>"
    #hàm so sánh
    def __gt__(self, other):
        return self.age > other.age
    
            
# student_one = Student("Bob", 23)
# student_two = Student("Mary", 33)
# print(student_one.name)
# print(student_one)
# print(student_one.age > student_two.age)

student_one = Student("An", 23, "Viet Nam")
Student.show_info(student_one)
student_one.show_info()


class People:
    def __init__(self,year):\
        self.year = year
        
    @property                   # Property chỉ chuyền vào khi chỉ có biến self thôi
                                # Khi chuyền vào @property thì khi sử dụng hàm thì không cần dấu ngoặc tròn                    
    def age(self):
        return 2024 - self.year
    
people_one = People(2005)
age = people_one.age
print(age)

"""Kế thừa"""
class Human:
    def __init__(self, name):
        self.name = name
    def __str__(self) -> str:
        return f"Name: {self.name}"

class Peoople(Human):
    def __init__(self, name,age):
        super().__init__(name)
        self.age = age

    def __str__(self) -> str:
        return f"Name: {self.name}, Age: {self.age}"

peoople_one = Peoople("Bob",23)        
print(peoople_one)

#Phân biệt repr với str
class Studentt:
    def __init__(self, name):
        self.name = name
    def repr(self):
        return f"<Student(Name: {self.name})>"
    def __str__(self) -> str:
        return f"Name: {self.name}"
        
student_one = Studentt("Bob")    
print(student_one.__str__)

class Animal:
    count = 0
    
    def __init__(self):
        Animal.count += 1
        
a1 = Animal()
print(Animal.count)
a2 = Animal()
print(Animal.count)


#FILE

# fp = open("test.txt", mode="r")
# a = fp.read()
# print(a)

# fp.close()


lst = ["a", 1, True, "c", 4.5]

fp = open("data.txt", mode="w")
fp.write(" - ".join(map(str, lst)))

fp.close()

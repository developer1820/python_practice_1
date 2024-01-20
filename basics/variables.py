# class Test:
#     """Represents Test class"""
#     # def __init__(self, name):
#     #     self.name = name  # 1st place inside constructor using self

#     def my_age(self, age):
#         self.age = age  # 2nd place inside instance method using self
#         # print(self.age)


# t1 = Test("John")
# t1.my_age(30)
# t1.marks = 50  # 3rd place outside class using object reference

# t2 = Test("Jack")
# t2.my_age()


# print(f"My Name is {t1.name}, age is {t1.age} and I got {t1.marks} marks")

# # print(f"My Name is {t2.name}, age is {t2.age} and I got {t2.marks} marks")

# name = "Aarti"
# print(name)

# num1 = 20
# print(num1)

# names = ["John", "Jack", "Something"]  # obejct creation
# names.append("Hello")
# names.insert(1, "Nope")


# def calculator(num1, num2):
#     return num1 + num2


# print(calculator(10, 20))
# print(calculator(10, 20))
# print(calculator(10, 20))
# print(calculator(10, 20))
# print(calculator(10, 20))

# name = "Hello"
# age = "30"


# def my_details():
#     print(name, age)


# my_details()


# class Test:
#     name = "Hello"
#     age = "30"

#     def my_details(self):
#         print(Test.name, Test.age)
#         print(self.name, self.age)


# t1 = Test()
# t1.my_details()

class Pupils():

    """ This class contain inormation about pupils."""

    hod = "Mr John"  # static variable
    school_name = "Montessory School"  # static variable

    def __init__(self):  # constructor
        self.subject = "Maths"  # instance variable
        Pupils.teacher = "Mr Adam"  # static variable

    def pupil_name(self, name):  # instace method
        self.pupil_name = name  # instance variable
        Pupils.principal_name = "Mr Mathew"  # static variable

    @classmethod
    def pupils_class(cls, standard):
        cls.pupil_standard = standard  # static variable
        cls.library = "Room number 8"  # static variable
        #          or
        Pupils.library = "Room number 8"  # static variable
        num_table = 2  # local variable
        # print(f"I have {num_table} tables in my class ")
        return num_table

    @staticmethod
    def school_address():
        Pupils.school_address = "2, abc street"  # static variable


pupil1 = Pupils()  # object creation with object referance variable
pupil1.pupil_name("Hiyan")
result = pupil1.pupils_class("Standard 1")
pupil1.school_address()
pupil1.age = 4  # instance variable

print(f"""My name is {pupil1.pupil_name}, I am {pupil1.age} year old,
      My HOD is {Pupils.hod} and my principal is {Pupils.principal_name},
      My school address is {Pupils.school_address},
      I am studying in {pupil1.pupil_standard} at {Pupils.school_name},
      I love {pupil1.subject}, {Pupils.teacher} teaches me {pupil1.subject}.
      My library is in {Pupils.library}. I have {result} table in my class.
      And I enjoy going to school.
      """)

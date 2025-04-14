# # # 1. Class name begins with a capital letter

# # class Patro:
# #     name="Sarthak"
# #     age=25

# # S1=Patro() # Creating an object of the class Patro
# # S2=Patro() # Both instances will have access to same blueprint defined in the class hence even if instances are different name will be same
# # print("S1 memory location:",S1) 
# # print("S2 memory location:",S2)

# # print("S1:",S1.name)
# # print("S2:",S2.name)

# # -------------------------------------------------------------------------------------------------------------------

# # 2. Contructors are executed at the time of creation of instance: __init__ function is the constructor
# # which is called at the time of creation of object 
# #  IF we dont create constructor then Python automatically creates a constructor


# # Generally we create only single constructor in class
# class NotFixed:
#     #  Default constructor
#     def __init__(self):
#         print("This is a default constructor, if we don't create it python will create it by default")
#     # Parameterised Constructor
#     def __init__(self,namex): # self or anything we can call to the first paramater, which is a reference to the 
#                               # current instance of the class and is used to access variables and methods from the class
#         self.name=namex
#         print("Self is pointing to:", self.name)


# s1=NotFixed("Sarthak")
# s2=NotFixed("Riya")
# s3=NotFixed("Rakesh")
# print(s3.name)

# # ------------------------------------------------------------------------------------------------------------------------
# #  Class vs object attributes
# #  * object attributes have higher preference than class attributes

class School:
    school_name="NCJPS School" # class level attribute to store common variables for all objects 
    stud_name="Anonymous"      
    def __init__(self,stud_name):
        self.stud_name=stud_name
    def demoFunction(self):
        print("This is a demo function inside class, Namaste",self.stud_name)
stud1=School("Sarthak")
stud1.demoFunction()
print(stud1.stud_name)
print(stud1.school_name) 
print(School.school_name)
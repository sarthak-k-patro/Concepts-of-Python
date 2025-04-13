# # 1. Class name begins with a capital letter

# class Patro:
#     name="Sarthak"
#     age=25

# S1=Patro() # Creating an object of the class Patro
# S2=Patro() # Both instances will have access to same blueprint defined in the class hence even if instances are different name will be same
# print("S1 memory location:",S1) 
# print("S2 memory location:",S2)

# print("S1:",S1.name)
# print("S2:",S2.name)

# -------------------------------------------------------------------------------------------------------------------

# 2. Contructors are executed at the time of creation of instance: __init__ function is the constructor
# which is called at the time of creation of object 
#  IF we dont create constructor then Python automatically creates a constructor


# Generally we create only single constructor in class
class NotFixed:
    #  Default constructor
    def __init__(self):
        print("This is a default constructor, if we don't create it python will create it by default")
    # Parameterised Constructor
    def __init__(self,namex): # self or anything we can call to the first paramater, which is a reference to the 
                              # current instance of the class and is used to access variables and methods from the class
        self.name=namex
        print("Self is pointing to:", self.name)


s1=NotFixed("Sarthak")
s2=NotFixed("Riya")
s3=NotFixed("Rakesh")
print(s3.name)

# ------------------------------------------------------------------------------------------------------------------------

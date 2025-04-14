#  Static methods are methods that dont use the self parameter
# They are used at class level
#  Here decorator is used to change the behaviour of normal function by converting it into statis
#  but you can see its not changing the function behaviour its just extending the behaviour without permanently modifying it
class College:
    @staticmethod # after using @staticmethod decorator we can see self paramater is not required
    def hello():  # 'self' parameter not required
        print("Hello, I am a function inside Class")
obj1=College()
obj1.hello()

# ------------------------------------------------------------------------------------------------------------------
# Abstraction , Encapsulation, Inheritance and Polymorphism

# 1. Abstraction: Hiding internal functioning, basically functioning jo hide hoti hai inside class
# 2. Encapsulation: Binding data with methods, basically data ko methods se bind karna. or variables ko functions mai use karna and unke saath bind krna
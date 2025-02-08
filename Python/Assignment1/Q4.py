'''4. How does Python enforce access control to class attributes, and what is the difference between public,
protected, and private attributes?'''

# Python enforces access control to class attributes by using the following naming conventions:
# 1. Public attributes: 
#         - Directly accessible from outside the class using dot notation.
#         - Defined without any underscores before the attribute name.
# 2. Protected attributes: 
#         - Accessible within the class and its subclasses.
#         - Defined using a single underscore before the attribute name.
# 3. Private attributes:
#         - Accessible only within the class, but can be accessed outside using getter and setter methods.
#         - To access them, name mangling can be used by using the format: _ClassName__private_attr.
#         - Defined using a double underscore before the attribute name. 


# # Example: -
# print('''Name: Sidhanta Barik, RegNo: 2241002049
# -----------------------------------------''')
# class MyClass:
#     def __init__(self):
#         self.public_attr = "Public attribute"
#         self._protected_attr = "Protected attribute"
#         self.__private_attr = "Private attribute"

#     def get_private_attr(self):
#         return self.__private_attr
    
# obj = MyClass()
# print(obj.public_attr)  
# print(obj._protected_attr) 
# # print(obj.__private_attr)  
# print(obj._MyClass__private_attr)
# print(obj.get_private_attr())  

# Name: Sidhanta Barik, RegNo: 2241002049
# -----------------------------------------
# Public attribute
# Protected attribute
# # AttributeError: 'MyClass' object has no attribute '__private_attr'.
# Private attribute
# Private attribute

'''NOTE: The double underscore before the attribute name is used to invoke name mangling, which makes the attribute name unique to the class to avoid conflicts with subclasses. To access private attributes from outside the class, you can use the name mangling convention: _ClassName__private_attr.
'''
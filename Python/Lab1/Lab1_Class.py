# 28/1/25

'''
Class:  It is a type of blueprint, used to design the structure and layout of an object.
        
Object: An object is an instance of a class.
        An object is a bundle of related attributes(variables) and methods(functions).
'''

# class Mobile:
#     properties(attributes) -> Battery, Brand, Storage
#     methods -> calling, texting, gaming 

'''
Attributes: They are similar to variables to describe what the object has.
            Eg: If we have a mobile object, some of its attributes can be battery, brand, storage, etc.

            Objects also have the capability to do things.
            They have methods which are functions belonging to that object.
            Eg; if we have a mobile objects, some of its methods can be calling, texting, gaming, etc.
'''

# class BulletEcho: #By Convention, the first letter of the class is Capitalized.
#     def __init__(self, name, level, weapon):
#         '''
#         When we first create a class object in python, it will always run the dunder init method first.
#         (In Python, a dunder method is a method that has double underscores(__) before and after its name.)
#         It is a constructor method which initializes the object and also handles the input. It will be called automatically whenever an object of the class is created.

#         A 'Constructor' is a special method used to initialize the attribute of an object when it is created.
#         '''
        
#         self.name = name
#         self.level = level
#         self.weapon = weapon

#         '''
#         'self' variable is supplied automatically and is always placed as the first variable.
#         self can be replaced by any other name. However, it is chosen as per convention.
#         It is a default variable that contains the memory address of the instance(object) of the current class.
#         self contains the memory address of the instance.
#         '''

#     def highlevel(self):
#         if self.level>75:
#             print(f'{self.name} is a high level character.')
#         else:
#             print(f'{self.name} is a normal level character.')

# char1 = BulletEcho('Bastion', 87, 'Machine Gun')
# char2 = BulletEcho('FireFly', 76, 'Sniper')
# char3 = BulletEcho('Levi', 71, 'Assualt Rifle')

# print(char1.name) # Bastion
# print(char1.level) # 87
# print(char1.weapon) # Machine Gun
# char1.highlevel() # Bastion is a high level character.
# char2.highlevel() # FireFly is a high level character.
# char3.highlevel() # Levi is a normal level character.


'''
Inheritance: It is used to inherit the properties of an existing class along with having new properties.
'''
# class BulletEcho:
#     def __init__(self, name, level, weapon):
#         self.name = name
#         self.level = level
#         self.weapon = weapon

#     def highlevel(self):
#         if self.level>75:
#             print(f'{self.name} is a high level character.')
#         else:
#             print(f'{self.name} is a normal level character.')

# class MoreProps(BulletEcho):
#     def __init__(self, name, level, weapon, health, armor):
#         super().__init__(name, level, weapon)
#         self.health = health
#         self.armor = armor

# char1 = BulletEcho('Bastion', 87, "Machine Gun")
# # print(char1.health) # AttributeError: 'BulletEcho' object has no attribute 'health'
# char2 = MoreProps('Firefly', 87, "Sniper", 100, 80)
# print(char2.health) # 100
# char3 = MoreProps('Levi', 71, 'Assualt Rifle', 100, 80)
# char3.highlevel() # Levi is a normal level character.


# 1/2/25

'''
Encapsulation: used to encapsulate particular attribute to restrict access to everyone
'''
# class BulletEcho: 
#     def __init__(self,name,level,weapon):
#         self.name=name
#         self.level=level
#         self.__weapon=weapon ## PRIVATE
#     def get_weapon(self):
#         return f'{self.name} uses {self.__weapon}'
# char1=BulletEcho("bastion",87,"machine gun")
# print(char1.weapon) # AttributeError: 'BulletEcho' object has no attribute 'weapon'

# NOTE: '__weapon' was a private attribute .To get access to private attributes in python we use getter methods


'''
Polymorphism: poly means many and morph means forms and shapes.
              It means that different classes can have methods with the same name, but the characteristics of the methods would be different.
'''
# class Bulletecho: 
#     def __init__(self,name,level,weapon):
#         self.name=name
#         self.level=level
#         self.weapon=weapon
#     def highlevel(self):
#         if self.level > 75:
#             print(f"{self.name} is a high level character")
#         else:
#             print(f"{self.name} is a normal level character")
#     def gametype(self):
#         if self.level>75:
#             print(f'{self.name} is playing in the arena mode')
#         else:
#             print(f'{self.name} is playing in the solo mode')

# class MoreProps(Bulletecho):
#     def __init__(self,name,level,weapon,health,armor):
#         super().__init__(name,level,weapon)
#         self.health=health
#         self.armor=armor

# char1=Bulletecho("bstion",87,"machine gun")
# char2=MoreProps('firefly',76,'Sniper',100,50)
# # print(char1.health) # AttributeError: 'Bulletecho' object has no attribute 'health'
# print(char2.health) # 100
# char1.gametype() # bstion is playing in the arena mode
# char2.gametype() # firefly is playing in the arena mode
'''-------------------------------xx---------------------------------'''

# class Bulletecho: 
#     def __init__(self,name,level,weapon):
#         self.name=name
#         self.level=level
#         self.weapon=weapon
#     def highlevel(self):
#         if self.level > 75:
#             print(f"{self.name} is a high level character")
#         else:
#             print(f"{self.name} is a normal level character")
#     def gametype(self):
#         if self.level>75:
#             print(f'{self.name} is playing in the arena mode')
#         else:
#             print(f'{self.name} is playing in the solo mode')

# class MoreProps(Bulletecho):
#     def __init__(self,name,level,weapon,health,armor):
#         super().__init__(name,level,weapon)
#         self.health=health
#         self.armor=armor
        
#     def gametype(self):
#         if self.health<25:
#             print(f'{self.name} activated god mode')
#         else:
#             print(f'{self.name} is playing in normal mode')

# char1=Bulletecho("bstion",87,"machine gun")
# char2=MoreProps('firefly',76,'Sniper',100,0)
# char1.gametype() # bstion is playing in the arena mode
# char2.gametype() # firefly is playing in normal mode


'''Counting the number of objects created'''
# class Bulletecho: 
#     count=0
#     def __init__(self,name,level,weapon):
#         self.name=name
#         self.level=level
#         self.weapon=weapon
#         Bulletecho.count+=1
    
#     def highlevel(self):
#         if self.level > 75:
#             print(f"{self.name} is a high level character")
#         else:
#             print(f"{self.name} is a normal level character")
#     def gametype(self):
#         if self.level>75:
#             print(f'{self.name} is playing in the arena mode')
#         else:
#             print(f'{self.name} is playing in the solo mode')

# class MoreProps(Bulletecho):
#     def __init__(self,name,level,weapon,health,armor):
#         super().__init__(name,level,weapon)
#         self.health=health
#         self.armor=armor
        
#     def gametype(self):
#         if self.health<25:
#             print(f'{self.name} activated god mode')
#         else:
#             print(f'{self.name} is playing in normal mode')

# char1=Bulletecho("1st",87,"machine gun")
# char2=Bulletecho("2nd",87,"w2")
# char3=Bulletecho("3rd",87,"w3")
# char4=MoreProps('p1',76,'Sniper',100,0)
# char5=MoreProps('p2',76,'S2r',100,0)
# print(Bulletecho.count) # 5
# print(MoreProps.count) # 5
'''-------------------------------xx---------------------------------'''

# class Bulletecho: 
#     count=0
#     def __init__(self,name,level,weapon):
#         self.name=name
#         self.level=level
#         self.weapon=weapon
#         self.count+=1 # It does not increment the count of the class, it creates a new instance variable count of a particular object.
    
#     def highlevel(self):
#         if self.level > 75:
#             print(f"{self.name} is a high level character")
#         else:
#             print(f"{self.name} is a normal level character")
#     def gametype(self):
#         if self.level>75:
#             print(f'{self.name} is playing in the arena mode')
#         else:
#             print(f'{self.name} is playing in the solo mode')

# class MoreProps(Bulletecho):
#     def __init__(self,name,level,weapon,health,armor):
#         super().__init__(name,level,weapon)
#         self.health=health
#         self.armor=armor
        
#     def gametype(self):
#         if self.health<25:
#             print(f'{self.name} activated god mode')
#         else:
#             print(f'{self.name} is playing in normal mode')

# char1=Bulletecho("1st",87,"machine gun")
# char3=Bulletecho("3rd",87,"w3")
# char4=MoreProps('p1',76,'Sniper',100,0)
# char5=MoreProps('p2',76,'S2r',100,0)
# print(MoreProps.count) # 0 (As count is never updated)
# print(Bulletecho.count) # 0 (As count is never updated)


'''
Static method: A static method is a method which is bound to the class and not to any specific instance of the class(object,self).
               Thus, the function is put inside the class but it cannot access the instance of the class.
               It means that the static method exists independently from the instances ,for which it is called static.
               In the static method, the function does not need a self argument (it does not receive an implicit 1st argument).
               static method is a decorator and can be called directly using the class name 
'''
# class Bulletecho: 
#     def __init__(self,name,level,weapon):
#         self.name=name
#         self.level=level
#         self.weapon=weapon
#     def statement(self):
#         return 'I hope you are happy with the game'
# char1=Bulletecho("kiki",87,"machine gun")
# print(char1.statement()) # I hope you are happy with the game
# # print(Bulletecho.statement()) # TypeError: Bulletecho.statement() missing 1 required positional argument: 'self'
'''-------------------------------xx---------------------------------'''

# class Bulletecho: 
#     def __init__(self,name,level,weapon):
#         self.name=name
#         self.level=level
#         self.weapon=weapon
#     def statement():
#         return 'I hope you are happy with the game'
# char1=Bulletecho("kiki",87,"machine gun")
# print(Bulletecho.statement()) # I hope you are happy with the game
# print(char1.statement()) # TypeError: Bulletecho.statement() takes 0 positional arguments but 1 was given
'''-------------------------------xx---------------------------------'''

# class Bulletecho: 
#     def __init__(self,name,level,weapon):
#         self.name=name
#         self.level=level
#         self.weapon=weapon
#     @staticmethod
#     def statement(self):
#         return f'I hope you are happy with the game {self.name}'
# char1=Bulletecho("kiki",87,"machine gun")
# # print(Bulletecho.statement()) # TypeError: Bulletecho.statement() missing 1 required positional argument: 'self'
# # print(char1.statement()) # TypeError: Bulletecho.statement() missing 1 required positional argument: 'self'


'''
Self variable: is a default variable that contains the memory adddress of the instance of the current class 
               so we can use 'self' to refer to all the instance variables and methods
'''

'''
Constructor: is a special ,ethod that is used to initialize the instance variable of a class.
             In constructor, we create the instance variable and initialize with some starting value
             The 1st parameter of the constructor will be self variable that contains memory address of that instance
'''

'''
Types of variables:-
    * instance variables
    * class variables or static variable
'''
'''
Instance variables: are the variables whose separate copy is created in every instance or object.
'''
# class Sample:
#     def __init__(self): # constructor method
#         self.x=10
#     def modify(self): # instacnce method
#         self.x+=1

# s1=Sample()
# s2=Sample()
# print("x in s1=",s1.x)
# print("x in s2=",s2.x)
# s1.modify()
# print("x in s1=",s1.x)
# print("x in s2=",s2.x)
# s1.modify()
# print("x in s1=",s1.x)
# print("x in s2=",s2.x)
# # x in s1= 10
# # x in s2= 10
# # x in s1= 11
# # x in s2= 10
# # x in s1= 12
# # x in s2= 10
'''
In the above example , x is an instance var and if we create 2 instances , there will be 2 copies of x in these instances.
When we modify we modify the copy of x in one instance , it will not modify the copy of  x  in the other instance
'''

'''
class variables: unlike instance var, class variables are the variables whose single copy is available to all instances of the class.
                 If we modify the copy of class var in an instance, it will modyfy all the copies in other instances as well
'''
# class Sample :
#     x=10 # class variable 

#     @classmethod
#     def modify(cls):
#         cls.x+=1

# s1=Sample()
# s2=Sample()
# print("x in s1=",s1.x)
# print("x in s2=",s2.x)
# s1.modify()
# print("x in s1=",s1.x)
# print("x in s2=",s2.x)
# s1.modify()
# print("x in s1=",s1.x)
# print("x in s2=",s2.x)
# # x in s1= 10
# # x in s2= 10
# # x in s1= 11
# # x in s2= 11
# # x in s1= 12
# # x in s2= 12


'''
Types of Methods: -
    1) Instance methods:
        i) Accessor methods
        ii) Mutator methods
    2) Class methods
    3) Static methods
'''
'''
1) Instance methods: 
    * are the methods which act upon the instance var of the class.
    * are bound to instances and hence are called instancename.method().
    * since instance var are available in the instance , instance methods needs to know the mem address of the instance.
    * this is provided with self variable

    i) Accessor methods:
        * simply access or read the data of the var
        * they do not modify the data in the var
        * also called getter methods
    ii) Mutator methods:
        * are the methods which not only read the data but also modify them
        * also called setter methods
'''
# class Student :
#     def __init__(self,n=".",m=0):
#         self.name=n
#         self.marks=m
#     def display(self): # instance method
#         print("hi ",self.name)
#         print("your marks: ",self.marks)
#     def calculate(self):
#         if self.marks>=600:
#             print("1st grade")
#         elif self.marks>=500:
#             print("2nd grade")
#         elif self.marks>=350:
#             print("3rd grade")
#         else:
#             print("fail")

# n=int(input("Enter no of students: "))
# i=0
# while i<n:
#     name=input("enter name: ")
#     marks=int(input("Enter marks: "))
#     s=Student(name,marks)
#     s.display()
#     s.calculate()
#     i+=1
#     print("_________________________________________________________________________")
# # Enter no of students: 3
# # enter name: Sid
# # Enter marks: 68
# # hi  Sid
# # your marks:  68
# # fail
# # _________________________________________________________________________
# # enter name: Baigan
# # Enter marks: 89
# # hi  Baigan
# # your marks:  89
# # fail
# # _________________________________________________________________________
# # enter name: Aloo
# # Enter marks: 580
# # hi  Aloo
# # your marks:  580
# # 2nd grade
# # _________________________________________________________________________
'''-------------------------------xx---------------------------------'''


# class Student:
#     def setName(self,name): # mutator method
#         self.name=name
#     def getName(self): # accessor method
#         return self .name
#     def setMarks(self,marks): # mutator method
#         self.marks=marks
#     def getMarks(self): # accessor method
#         return self .marks

# n=int(input("Enter no of students: "))
# i=0
# while i<n:
#     name=input("enter name :")
#     marks=int(input("Enter marks: "))
#     s=Student()
#     s.setName(name)
#     s.setMarks(marks)
#     print("hi ",s.getName())
#     print("your marks: ",s.getMarks())
#     i+=1
#     print("_________________________________________________________________________")
# # Enter no of students: 2
# # enter name :Sid
# # Enter marks: 840
# # hi  Sid
# # your marks:  840
# # _________________________________________________________________________
# # enter name :Aloo
# # Enter marks: 600
# # hi  Aloo
# # your marks:  600
# # _________________________________________________________________________


'''
2) Class methods:-
    * acts on the class level
    * thay act on class var or static variables
    * are written using @classmethod decorator above them
    * by default, the 1st parameter for class methods is cls which refers to class itself
'''
# class Bird:
#     wings=2 # class var
#     @classmethod
#     def fly(cls,name):
#         print('{} flies with {} wings'.format(name,cls.wings))

# Bird.fly("Virat") # Virat flies with 2 wings
# Bird.fly("Cow") # Cow flies with 2 wings


'''
3) Static methods: We need static methods, when the processing is at the class level but we need not involve the class or the instances.
                   used when some processes are related to class but doesnt need the class or instances to perform any work.
'''
# class Myclass:
#     n=0 # class var or static var
#     def __init__(self):
#         Myclass.n+=1
#     @staticmethod
#     def NOofObjects():
#         print("total instances : ",Myclass.n)
# obj1=Myclass() 
# Myclass.NOofObjects() # total instances :  1
# obj2=Myclass()
# Myclass.NOofObjects() # total instances :  2
# obj3=Myclass()
# Myclass.NOofObjects() # total instances :  3
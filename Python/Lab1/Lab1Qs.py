# 28/1/25

'''
Q1)Create a class Mobile having: 
    atributes: brand, battery, storage.
    methods: calling, texting, gaming with the following conditions: 
        calling is possible if battery>25%
        texting is possible if battery>15%
        gaming is possible if battery>40% and storage>=64GB

i) Can I call on Samsung S23 having battery 30%? 
ii) Can I call on Redmi Note 13 having battery 10%? 
iii) Can I play games on Apple having battery 45% storage 32GB? 
'''

# class Mobile:
#     def __init__(self, brand, battery, storage):
#         self.brand = brand
#         self.battery = battery
#         self.storage = storage
    
#     def calling(self):
#         if self.battery > 25:
#             return True
#         else:
#             return False
#     def texting(self):
#         if self.battery > 15:
#             return True
#         else:
#             return False
#     def gaming(self):
#         if self.battery>40 and self.storage>='64GB':
#             return True
#         else:
#             return False

# m1 = Mobile("Samsung S23", 30, '64GB')
# m2 = Mobile("Redmi Note 13", 10, '32GB')
# m3 = Mobile("Apple", 45, '32GB')
# if(m1.calling()):
#     print(f"Calling is possible in {m1.brand} with {m1.battery}% battery.")
# else:
#     print(f"Calling is not possible in {m1.brand} with {m1.battery}% battery.")

# if(m2.calling()):
#     print(f"Calling is possible in {m2.brand} with {m2.battery}% battery.")
# else:
#     print(f"Calling is not possible in {m2.brand} with {m2.battery}% battery.")

# if(m3.gaming()):
#     print(f"Gaming is possible in {m3.brand} with {m3.battery}% battery and {m3.storage} storage.")
# else:
#     print(f"Gaming is not possible in {m3.brand} with {m3.battery}% battery and {m3.storage} storage.")

# # # OUTPUT:-
# # Calling is possible in Samsung S23 with 30% battery.
# # Calling is not possible in Redmi Note 13 with 10% battery.
# # Gaming is not possible in Apple with 45% battery and 32GB storage.


'''
Q2) Create a class 'Grandfather' having 2 attributes ag1, ag2 and 1 method mg1.
    Inherit 'Grandparent' properties in a class called 'Parent' having attributes ag1, ag2, ap1, ap2, ap3 and methods mg1, mp1, mp2.
    Inherit 'Parent' properties in a class called 'Child' having attributes ag1, ag2, ap1, ap2, ap3, ac1, ac2 and methods mg1, mp1, mp2, mc1, mc2.
'''
# class Grandfather:
#     def __init__(self, ag1, ag2):
#         self.ag1 = ag1
#         self.ag2 = ag2
#     def mg1(self):
#         print(f"Value of ag1 is {self.ag1}")
#     def mg2(self):
#         print(f"Value of ag2 is {self.ag2}")
# class Parent(Grandfather):
#     def __init__(self, ag1, ag2, ap1, ap2, ap3):
#         super().__init__(ag1, ag2)
#         self.ap1 = ap1
#         self.ap2 = ap2
#         self.ap3 = ap3
#     def mp1(self):
#         print(f"value of ap1 is {self.ap1}")
#     def mp2(self):
#         print(f"value of ap2 is {self.ap2}")
#         print(f"value of ap3 is {self.ap3}")
# class Child(Parent):
#     def __init__(self, ag1, ag2, ap1, ap2, ap3, ac1, ac2):
#         super().__init__(ag1, ag2, ap1, ap2, ap3)
#         self.ac1 = ac1
#         self.ac2 = ac2
#     def mc1(self):
#         print(f"Value of ac1 is {self.ac1}")
#     def mc2(self):
#         print(f"Value of ac2 is {self.ac2}")

# c1 = Child(1,2,3,4,5,6,7)
# c1.mg1()
# c1.mg2()
# c1.mp1()
# c1.mp2()
# c1.mc1()
# c1.mc2()
# # Value of ag1 is 1
# # Value of ag2 is 2
# # value of ap1 is 3
# # value of ap2 is 4
# # value of ap3 is 5
# # Value of ac1 is 6
# # Value of ac2 is 7


'''Using real life attributes in Q2:-'''
class Grandfather:
    def __init__(self, Gname, Gsurname, Gmoney):
        self.Gname = Gname
        self.Gsurname = Gsurname
        self.Gmoney = Gmoney
    def getGname(self):
        print(f"Name of Grandfather: {self.Gname} {self.Gsurname}")
    def getGmoney(self):
        print(f"Money of Grandfather: {self.Gmoney}")

class Parent(Grandfather):
    def __init__(self, Gname, Gsurname, Gmoney, Pname, Pmoney):
        super().__init__(Gname, Gsurname, Gmoney)
        self.Pname = Pname
        self.Pmoney =  Gmoney+Pmoney
    def getPname(self):
        print(f"Name of Parent: {self.Pname} {self.Gsurname}")
    def getPmoney(self):
        print(f"Money of Parent: {self.Pmoney}")

class Child(Parent):
    def __init__(self, Gname, Gsurname, Gmoney, Pname, Pmoney, Cname, Cmoney):
        super().__init__(Gname, Gsurname, Gmoney, Pname, Pmoney)
        self.Cname = Cname
        self.Cmoney = Gmoney+Pmoney+Cmoney
    def getCname(self):
        print(f"Name of Child: {self.Cname} {self.Gsurname}")
    def getCmoney(self):
        print(f"Money of Child: {self.Cmoney}")

c1 = Child("ABC", "Barik", 5000, "PQR", 100, "Sid", 30)
c1.getGname() # Name of Grandfather: ABC Barik
c1.getPname() # Name of Parent: PQR Barik
c1.getCname() # Name of Child: Sid Barik
c1.getGmoney() # Money of Grandfather: 5000
c1.getPmoney() # Money of Parent: 5100
c1.getCmoney() # Money of Child: 5130
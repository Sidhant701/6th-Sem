# 4/3/25

class Time:
    def __init__(self, hour = 0, minute = 0, second = 0):
        '''
        Properties hour, minute & second look like data attributes to programmers working with objects of class Time. However, properties are implemented as methods, so, they may contain additional logic such as specifying the format in which to return a data attribute value or validating a new value before using it to modify a data attribute.
        '''
        self.hour = hour # 0-23
        self.minute = minute # 0-59
        self.second = second # 0-59
        '''
        self.hour, self.minute & self.second appear to create hour, minute & second attributes for the objects of class Time. However, these statements actually call methods that implement the class' hour, minute & second property. Those method then create attributes _hour, _minute & _second that are meant to be used only inside the class.
        Python creates getter & setter methods to create these attributes.
        "Getter" methods are used to get the values.
        "Setter" methods are used to set the values after validation.
        '''

    def __str__(self):
        '''
        __str__ (dunder[double underscore] str) is a special method which is called when an Object is converted to String, such as when you output the object using the print() statement. __str__ implementation in this particular problem creates a string in 12hr clock format
        '''
        return (('12' if self.hour in (0, 12) else str(self.hour % 12)) +
                f':{self.minute:0>2}:{self.second:0>2}' +
                (' AM' if self.hour < 12 else ' PM'))

    # def __repr__(self):
    #     '''
    #     If a class does not provide the __str__ method and an object of the class is converted to a String, the class' __repr__ method is called instead.
    #     '''
    #     return (f'Time(hour={self.hour}, minute={self.minute}, ' +
    #             f'second={self.second})')

    @property
    def hour(self): # getter method, whose name is the property name
        '''
        property "hour" is implemented as a member. Each property(like hour) defines a getter method which gets, i.e., returns a data attribute value. 
        The getter method's name is the property name.
        '''
        return self._hour

    @hour.setter # @propertyName.setter
    def hour(self, hour):
        '''
        Define a setter method which sets the data attribute's value after validation
        '''
        if not(0<=hour<24):
            raise ValueError(f'Hour {hour} must lie between 0-23')
        self._hour = hour
        
    @property
    def minute(self):
        return self._minute

    @minute.setter
    def minute(self, minute):
        '''
        Define a setter method which sets the data attribute's value after validation
        '''
        if not(0<=minute<60):
            raise ValueError(f'Minute {minute} must lie between 0-59')
        self._minute = minute
        
    @property
    def second(self):
        return self._second

    @second.setter
    def second(self, second):
        '''
        Define a setter method which sets the data attribute's value after validation
        '''
        if not(0<=second<60):
            raise ValueError(f'second {second} must lie between 0-59')
        self._second = second
    
    def set_time(self, hour = 0, minute = 0, second = 0):
        '''
        We provide the method "set_time" as a convenient way to change all 3 attributes with a single method call
        '''
        self.hour = hour
        self.minute = minute
        self.second = second
        
# wake_up = Time(20, 58)
# print(wake_up) # 8:58:58 PM
# wake_up = Time(hour=20, minute=58)
# print(wake_up) # 8:58:58 PM

# wake_up = Time(hour=30, minute=58)
# print(wake_up) # ValueError: Hour 30 must lie between 0-23
# print(wake_up.hour) # ValueError: Hour 30 must lie between 0-23

# wake_up = Time(hour=9, minute=58)
# print(wake_up.hour)

t = Time()
t.set_time(20, 58, 30)
print(t) # 8:58:30 PM
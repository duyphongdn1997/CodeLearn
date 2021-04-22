# class Person:
#     def __init__(self, firstName, lastName):
#         self.firstName = firstName
#         self.lastName = lastName
#         self.fullName = '%s %s' % (firstName, lastName)
    
#     @Overload
#     def __init__(self, fullName):
#         first, last = fullName.split(' ')
#         self.firstName = first
#         self.lastName = last
#         self.fullName = fullName

class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
    
    @property
    def full_name(self):
        return '%s %s' % (self.first_name, self.last_name)
    
    @full_name.setter
    def full_name(self, name):
        first, last = name.split(' ')
        self.first_name = first
        self.last_name = last

A = Person('ABC','EDF')
A.full_name = 'ABC DCD'
print(A.full_name)
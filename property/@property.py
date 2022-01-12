class Person:
    def __init__(self, name):
        self._name = name

    @property ##property get assigns the function name
    def name(self):
        print('Getting name')
        return self._name

    @name.setter ##no need to define another function name, we can use fset of property 
    def name(self, value):
        print('Setting name to ' + value)
        self._name = value

    @name.deleter
    def name(self):
        print('Deleting name')
        del self._name

    # Set property to use get_name, set_name
    # and del_name methods
    # name = property(get_name, set_name, del_name, 'Name property')

p = Person('Adam')
print(p.name)
p.name = 'John'
del p.name
print(p.name)
class Person:
    def __init__(self, name):
        self._name = name

    def get_name(self):
        print('Getting name')
        return self._name

    def set_name(self, value):
        print('Setting name to ' + value)
        self._name = value

    def del_name(self):
        print('Deleting name')
        del self._name

    # Set property to use get_name, set_name
    # and del_name methods
    name = property(get_name, set_name, del_name, 'Name property')  ## property assigns fget to get_name, fset to set_name, fdel to del_name

p = Person('Adam')
print(p.name)  ##instead of calling p.get_name we can use p.name
p.name = 'John' ##instead of calling p.set_name we can use p.name and assign new value to set it
del p.name  ##instead of calling p.del_name we can use del p.name to delete value associated with it.
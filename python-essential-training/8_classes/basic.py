class Animal:
    def __init__(self, **kargs):
        self._type = kargs['type'] if 'type' in kargs else 'generic_animal'
        self._name = kargs['name'] if 'name' in kargs else 'generic_name'
        self._sound = kargs['sound'] if 'sound' in kargs else 'generic sound'
        
    def type(self):
        return self._type
    def name(self):
        return self._name
    def sound(self):
        return self._sound
    

def main():
    my_animal = Animal(type="pig", name="george", sound="grwwow")
    print (my_animal.name())
    
if __name__ == '__main__':
    main()
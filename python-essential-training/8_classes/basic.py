class Animal:
    def __init__(self, type, name, sound):
        self._type = type
        self._name = name
        self._sound = sound
        
    def type(self):
        return self._type
    def name(self):
        return self._name
    def sound(self):
        return self._sound
    

def main():
    my_animal = Animal('pig', 'george', 'grrw')
    print (my_animal.name())
    
if __name__ == '__main__':
    main()
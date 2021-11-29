class Animal:
    static_arr = [1,2,3]
    def __init__(self, **kargs):
        if 'type' in kargs:
             self._type = kargs['type']
        if 'name' in kargs:
            self._name = kargs['name']
        if 'sound' in kargs:
            self._sound = kargs['sound']
        
    def type(self, t=None):
        if t: self._type = t
        try:
            return self._type
        except AttributeError:
            return None
    def name(self, n=None):
        if n: self._name = n
        try:
            return self._name
        except ArithmeticError:
            return None
    def sound(self, s):
        if s: self._sound = s
        try:
            return self._sound
        except AttributeError:
            return None
    
class Duck(Animal):
    def __init__(self, **kargs):
        self._type = 'duck'
        if 'type' in kargs: del kargs['type']
        super().__init__(**kargs)

# reverse string class that extends str
class RevStr(str):
    def __str__(self):
        return self[::-1]

def main():
    my_animal = Animal(type="pig", name="george", sound="grwwow")
    my_generic_animal = Animal()
    
    my_animal.static_arr[0] = 999
    
    print (my_animal.name())
    print (my_generic_animal.static_arr)
    
    my_animal.name('alex')
    print(my_animal.name())
    
    duck = Duck(name="fred", sound="whoack")
    
    print(duck.type())
    
    my_str = RevStr("abc")
    print(my_str) # cba
    
if __name__ == '__main__':
    main()
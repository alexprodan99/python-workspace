class Animal:
    static_arr = [1,2,3]
    def __init__(self, **kargs):
        self._type = kargs['type'] if 'type' in kargs else 'generic_animal'
        self._name = kargs['name'] if 'name' in kargs else 'generic_name'
        self._sound = kargs['sound'] if 'sound' in kargs else 'generic sound'
        
    def type(self, t=None):
        if t: self._type = t
        return self._type
    def name(self, n=None):
        if n: self._name = n
        return self._name
    def sound(self, s):
        if s: self._sound = s
        return self._sound
    

def main():
    my_animal = Animal(type="pig", name="george", sound="grwwow")
    my_generic_animal = Animal()
    
    my_animal.static_arr[0] = 999
    
    print (my_animal.name())
    print (my_generic_animal.static_arr)
    
    my_animal.name('alex')
    print(my_animal.name())   
if __name__ == '__main__':
    main()
class my_str:
    def __init__(self, s):
        self._s = s
    def __repr__(self) -> str:
        return f'this is the representation of {self._s} 😃'
    def __str__(self) -> str:
        return f'this is the str of {self._s}'
def main():
    # numeric functions
    x = '47'
    y = int(x)
    z = 2.3
    print(f'x={x} and is of type {type(x)}')
    print(f'y={y} and is of type {type(y)}')
    print(f'z={z} and is of type {type(z)}')
    
    x = -123
    print(f'abs(x)={abs(x)}')
    
    x = 7
    y = 2
    
    (div, mod) = divmod(x,y) # div + modulus in same operation
    
    print (f'res={(div,mod)}')
    
    # complex numbers
    x = 2 + 3j
    y = 3 + 4j
    print (x + y) # 5 + 7j
    
    x = complex(2,3)
    y = complex(3,4)
    print (x + y) # 5 + 7j
    
    
    # string functions
    s = "123"
    # print the representation of s
    print(repr(s)) # '123'
    
    s = my_str('aaa')
    print(repr(s)) # this is the representation of aaa 😃
    print(s) # this is the str of aaa
    # if you don't have str implementation then print(s) will print repr, if repr is not overrided either will use default implementation
    
    
    # ascii representation
    print(ascii(s)) # this is the representation of aaa \U0001f603
    
    print(chr(128406)) # 🖖 (unicode representation)
    print(ord('🖖')) # 128406
    
    
    x = (1,2,3,4,5)
    y = list(reversed(x))
    z = sum(x)
    a = max(x)
    b = min(x)
    c = any(x) # returns True is any element is True (!= 0 False)
    d = all(x) # all true => True
    e = zip(x,y) # makes a dictionary from two lists
    print(x)
    print(y)
    print(z)
    print(a)
    print(b)
    print(c)
    print(d)
    for k,v in e:
        print(f'{k} - {v}')
        
        
    animals = ('cat', 'dog', 'rabbit')
    # index + value
    for i,v in enumerate(animals):
        print(f'{i} - {v}')
    
    
    
    
    x = 123
    y = 123
    print(type(x))
    print(isinstance(x, int))
    # same value for id(x) and id(y)
    print (id(x))
    print (id(y))
    
    # not same value for id(x) and id(y)
    x = [1,2,3]
    y = [1,2,3]
    print (id(x))
    print (id(y))
    
    # same value for id(x) and id(y)
    x = [1,2,3]
    y = x
    print (id(x))
    print (id(y))
    
    # same value for id(x) and id(y)
    x = '123'
    y = '123'
    print (id(x))
    print (id(y))
    
if __name__ == '__main__':
    main()
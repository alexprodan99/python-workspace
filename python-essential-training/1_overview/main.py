#!/usr/bin/env python3

# above is the shebang line => for unix systems (in this example env is used for getting path of python3)
# another way to write this line (hardcoded path to python)
#!/usr/local/bin/python3
import platform
import random

class Duck:
    # self is not defined here
    age = 10
    # by default if you have multiple __init__ functions python will consider just the last defined one
    # you can declaare in just one single __init__function *args and handle all cases inside one single class constructor
    def __init__(self, name):
        self.name = name

    def quack(self):
        print(f'{self.name} is quacking!')
    def walk(self):
        print(f'{self.name} is walking!');


# when you are declaring a default value
# pay attention that first parameter can have a default value only if all parameters after it has a default value
def generate_random_int(low, high=10):
    return random.randint(low, high)

def main():
    # for getting operating system and python version details
    print('hello world. We are on {} and python version is: {}'.format(platform.platform(), platform.python_version()))
    var = 2
    print('Hello world %d' %var)
    print(f'Hello world {var}')
    print('Hello world %d %d %d' %(var, var, var))
    # blocks are not defining scope in python (functions does)
    if 1 < 2:
        z = 2
    print(z)
    x = 10
    y = 20
    if x < y:
        print("{} is less than {}".format(x,y))
    elif x > y:
        print("{} is greater than {}".format(x,y))
    else:
        print("{} is equal to {}".format(x,y))
        
    # loops => while + for
    n = 0
    while (n < 5):
        print(n)
        n += 1
    
    a = 1
    b = 2
    # it will get in a + b previous value of a, not the updated one
    # so that you will not need to declare aux variables
    a, b = b, a + b
    print(a)
    print(b)
    
    words = ['aaa', 'bbb', 'ccc']
    for word in words:
        print (word)
    for i in range(len(words)):
        print(words[i])
    for i in range(0, len(words)):
        print(words[i])
        
    print('my random number is {}'.format(generate_random_int(0)))
    
    donald = Duck('donald')
    donald.walk()
    donald.quack()
    print(donald.age) # 10
    

if __name__ == '__main__': main()
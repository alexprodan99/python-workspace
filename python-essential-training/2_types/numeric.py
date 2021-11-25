from decimal import *

def main():
    a = 7
    b = 2
    print (f'{a} + {b} = {a+b}')
    print (f'{a} - {b} = {a-b}')
    print (f'{a} * {b} = {a*b}')
    print (f'{a} / {b} = {a/b}') # 3.5
    print (f'{a} // {b} = {a//b}') # 3 
    print (f'{a} ^ {b} = {a**b}')
    
    
    val = .1 + .1 + .1 - .3
    print(val) # is not zero exactly => don't use float type for money
    # how to solve this problem ?
    a = Decimal('.1')
    b = Decimal('.3')
    val = a + a + a - b
    print(val) # 0.0



if __name__ == '__main__':
    main()
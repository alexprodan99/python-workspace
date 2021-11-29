def main():
    my_str = "Hello World"
    print(my_str.swapcase())
    my_str = "aaa"
    print(my_str.upper())
    my_str = "alex"
    print(my_str.capitalize())
    my_str = "aaa"
    print(my_str.title())
    my_str = "Aaa"
    print(my_str.casefold())
    
    print(id(my_str))
    # concat (another way)
    s = 'aaaa' 'bbbb'
    print(s)
    
    
    # some format examples
    var1 = 12
    var2 = 24
    my_str = "var1 is {} and var2 is {}"
    
    print(my_str.format(var1, var2))
    
    my_str = "var1 is {0} and var2 is {1}"
    print(my_str.format(var1, var2))
    
    my_str = "var1 is {1} and var2 is {0}"
    print(my_str.format(var1, var2))
    
    my_str = "var1 is {var1} and var2 is {var2}"
    print(my_str.format(var2=var2, var1=var1))
    
    # 5 to left and 5 to right (including digits of var1 and var2)
    my_str = "var1 is {0:<5} and var2 is {0:>5}"
    print(my_str.format(var1, var2))
    
    my_str = "var1 is {0:<05} and var2 is {0:>05}"
    print(my_str.format(var1, var2))
    
    my_str = "var1 is {0:<+05} and var2 is {0:>+05}"
    print(my_str.format(var1, var2))
    
    
    my_val = 31232131
    # 31,232,131
    print ('my_val is {:,}'.format(my_val))
    # 31.232.131
    print ('my_val is {:,}'.format(my_val).replace(',', '.'))
    
    my_val = 3.1415926
    print('my_val is {:.3f}'.format(my_val)) # 3.142
    
    my_val = 123
    print('hexa={:x}'.format(my_val))
    print('octa={:o}'.format(my_val))
    print('binary={:b}'.format(123))
    
    
    print(f'hexa={my_val:x}')
    print(f'octa={my_val:o}')
    print(f'binary={my_val:b}')
    
    # split and join examples
    my_str = "This is a very long string"
    print(my_str.split()) # separtor = space
    my_str = "This,is,a,very,long,string"
    print(my_str.split(","))
    
    strs = my_str.split(",")
    
    new_str = ":".join(strs)
    print(new_str)
    

if __name__ == '__main__':
    main()
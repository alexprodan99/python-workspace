def main():
    # Arithmetic operators
    a = 7
    b = 2
    
    print(f'{a} + {b} = {a+b}')
    print(f'{a} - {b} = {a-b}')
    print(f'{a} * {b} = {a*b}')
    print(f'{a} / {b} = {a/b}')
    print(f'{a} // {b} = {a//b}')
    print(f'{a} % {b} = {a%b}')
    print(f'{a} ^ {b} = {a**b}')
    
    
    
    # Bitwise operators
    # &, |, ^, <<, >>
    print(f'{a} & {b} = {a&b}')
    print(f'{a} | {b} = {a|b}')
    print(f'{a} ^ {b} = {a^b}')
    print(f'{a} << {b} = {a<<b}')
    print(f'{a} >> {b} = {a>>b}')
    
    
    a = 0xff
    print(a) # 255
    # fill with zeroes and second arg is the minimum number of bits that will be displayed
    print(f'hex(a)={a:03x}') # 0ff
    print(f'bin(a)={a:09b}')
    
    
    
    # Comparison operators
    # >,<,==,!=, >=, <=
    
    # Boolean operators
    # and, or, not, in, not in, is, is not
    

if __name__ == '__main__':
    main()
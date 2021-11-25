def main():
    str = "alex"
    print (str.upper())
    print (str.lower())
    print (str) # alex => immutable
    
    str = "{1} {0}"
    print (str.format(1,2)) # 2 1
    
    str = "{} {}"
    print (str.format(1,2)) # 1 2
    
    str = 'single quotes'
    print (str)
    
    str = """
        multi line
        string
    """
    print(str) # newlines are included
    
    
    # 2 and 8 spaces and then 0 and other 8 spaces
    # < => left
    # > => right
    str = "{1:<9} {0:>9}"
    print(str.format(2,1))
    print(len(str.format(2,1))) # 19 (9 + 1 + 9)
    
    # with leading zeroes
    str = "{1:<09} {0:>09}"
    print(str.format(2,1))
    print(len(str.format(2,1))) # 19 (9 + 1 + 9)
    
    
    var = 2
    # starting with python 3.6 we have fstrings
    str = f'var={var}'
    print (str)
    a = 1
    b = 2
    str = f"{a:<09} {b:>09}"
    print(str)
    
    
if __name__ == '__main__':
    main()

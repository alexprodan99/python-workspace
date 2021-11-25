def main():
    x = True
    y = False
    print (x and y)
    print (x or y)
    x = 7 > 6
    print(x)
    x = None
    #False
    if x:
        print('True')
    else:
        print('False')
    y = True
    print (x and y) # None
    print (x or y) # True
    
    
    x = ""
    # False
    if x:
        print('True')
    else:
        print('False')
if __name__ == '__main__':
    main()
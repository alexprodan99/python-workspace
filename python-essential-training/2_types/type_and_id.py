def main():
    print (type(1))
    var = 123
    print (id(var))
    
    var1 = 123
    var2 = 123
    
    id1 = id(var1)
    id2 = id(var2)
    # returns same
    if id1 == id2:
        print('Same')
    else:
        print('Not same')
    
    # returns same obj
    if var1 is var2:
        print('Same obj')
    else:
        print('Not same obj')
    
    obj1 = {"aaa":111}
    obj2 = {"aaa":111}
    # Not same obj
    if obj1 is obj2:
        print('Same obj')
    else:
        print('Not same obj')

    # it's a dictionary
    if (isinstance(obj1, dict)):
        print("It's a dictionary")
if __name__ == '__main__':
    main()
    
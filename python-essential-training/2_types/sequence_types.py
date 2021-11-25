def main():
    vals = [1,2,3]
    vals[0] = 999
    for val in vals:
        print(val)
    vals = (1,2,3)
    # vals[0] = 1 => error
    
    for val in vals:
        print(val)
        
        
    x = range(5)
    for i in x:
        print(i)
    
    x = range(10,2)
    print(x)
    # will not enter the loop
    for i in x:
        print(i)
    
    
    # last arg is the step
    x = range(0,10,2)
    for i in x:
        print(i)
        
    my_list = list(range(5))
    
    for val in my_list:
        print(val)
        
    my_dict = {"aaa":1, "bbb":2, "ccc":3}
    for k,v in my_dict.items():
        # two ways to get value
        print(str(my_dict[k]) + " " + str(v))
    
    if "aaa" in my_dict:
        print ("Found!")

if __name__ == '__main__':
    main()

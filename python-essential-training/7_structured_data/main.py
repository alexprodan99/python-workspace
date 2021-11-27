def main():
    # lists => []
    # set => {}
    # tuple => ()
    
    # lists
    
    arr = [1,2,3]
    
    print(arr.index(2))
    
    arr.append(4)
    
    print(arr)
    
    arr.insert(0, -1) # insert on position 0 -1
    
    print(arr)
    
    arr.remove(-1) # remove first occurence
    
    print(arr)
    
    deleted = arr.pop()
    
    print(f"deleted={deleted}")
    print(arr)
    
    
    del arr[0]
    print(arr)
    del arr[0::]
    print(arr) # []
    
    words = ["aaa", "bbb", "ccc"]
    
    print (",".join(words))
    
    # dictionary
    grades = {
        "alex" : "A",
        "john" : "B"
    }
    
    for k,v in grades.items():
        print(v)
        
    for key in grades:
        print(grades[key])
        
    if "alex" in grades:
        print("Alex is present")
    
    
    # sets
    my_set1 = set("afsadasfgasdasda")
    my_set2 = set("cafsadasdasdasda")
    print(my_set1)
    print(my_set1 - my_set2)
    print(my_set1 | my_set2)
    print(my_set1 & my_set2)
    
    
    # list comprehenstion
    seq = range(100)
    my_list = [x for x in seq if x % 2 == 0]
    print(my_list)
    my_list = [(x, x**2) for x in seq]
    print(my_list)
    my_dict = {x : x**2 for x in seq}
    print(my_dict)
    my_set = {x for x in "anaconda"}
    print(my_set)
    
    # mixed structures
    my_list = ["aaa", 1, {1,2,3}, {"aaa":1, "bbb":2, "ccc":3}, (1,2,3)]
    my_dict = dict(aaa=my_list, bbb=[1,2,3])
    print(my_dict["aaa"])
    
if __name__ == '__main__':
    main()
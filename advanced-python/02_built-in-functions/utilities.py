def main():
    list1 = [1,2,3,4,5,0,6]
    
    # any element is True
    print(any(list1)) # True
    # all elements are True
    print(all(list1)) # False => 0
    # min element
    print(min(list1))
    # max element
    print(max(list1))
    # sum of all elements
    print(sum(list1))

if __name__ == '__main__':
    main()
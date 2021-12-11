def main():
    # list comprehension
    arr = [x ** 2 for x in range(10)]
    print(arr)
    arr = [x ** 2 for x in range(10) if x % 2 == 1]
    print(arr)
    
    # dict comprehension
    my_dict = {t : t ** 2 for t in range(10)}
    print(my_dict)
    my_dict = {t : t ** 2 for t in range(10) if t % 2 == 1}
    print(my_dict)
    
    
    # merge two dicts
    dict1 = {'aaa' : 1, 'bbb' : 2}
    dict2 = {'ccc' : 3}
    
    dict3 = {k:v for my_dict in (dict1, dict2) for k,v in my_dict.items()}
    print(dict3)
    
    
    # sets comprehension
    vals = [1,2,3,2,4]
    my_squares_set = {t ** 2 for t in vals}
    print(my_squares_set)
    
    my_str = 'fasdasfasdasdasdassagdffa'
    unique_chars = {t for t in my_str}
    print(unique_chars)

if __name__ == '__main__':
    main()
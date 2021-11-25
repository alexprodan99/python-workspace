def main():
    age = 10
    if age > 18:
        print('you can drink!')
    elif age > 10 and age < 18:
        print('you have to wait to drink')
    else:
        print('kid! are you crazy?')
    
    # conditional assignment
    text = 'TEXT1' if age > 10 else 'TEXT2'
    print(text)
    # you need to include else
    # text = 'TEXT1' if age > 10
    # print(text)
    
    
    
    my_list = [1,2,3]
    if 3 in my_list:
        print("Found!")
        
    if 5 not in my_list:
        print('Not found')
        
    my_list2 = [1,2,3]
    # check refs
    
    if my_list is my_list2:
        # it will not be printed
        print('Same')
    
    if my_list is not my_list2:
        print('Not Same')

if __name__ == '__main__':
    main()
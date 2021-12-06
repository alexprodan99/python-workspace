def main():
    my_list = [1,2,3,4]
    squares = list(map(lambda x: x ** 2, my_list))
    print(squares)
    
    myfunc = lambda x: x + 5
    print(myfunc(5)) # 10

if __name__ == '__main__':
    main()
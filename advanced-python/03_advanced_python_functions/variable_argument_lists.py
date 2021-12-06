
def addition(*args):
    result = 0
    for arg in args:
        result += arg
    return result

def main():
    res = addition(1,2,3,4)
    print(res)
    my_list = [1,2,3,4]
    res = addition(*my_list)
    print(res)

if __name__ ==  '__main__':
    main()
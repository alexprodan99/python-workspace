from typing import Type


def f1(a,b,c=0):
    print(a, b, c)

def zeroes(arr):
    # not working
    # for item in arr:
    #     item = 0
    
    for i in range(len(arr)):
        arr[i] = 0


def not_zeroes(arr):
    # trying to change reference will not change after the call arr values
    arr = [0 for i in range(len(arr))]

# variable number of arguments
def variable_args(*args):
    for arg in args:
        print(arg)

# keyword arguments
def kargs(**kargs):
    for key in kargs:
        print(f"{key}={kargs[key]}")

def sum(*args):
    sum = 0
    for arg in args:
        sum += arg
    return sum


# generator => function that is returning a stream of values and not just one single value
def inclusive_range(*args):
    numargs = len(args)
    start = 0
    step = 1
    
    if numargs < 1 or numargs > 3:
        raise TypeError("incorrect number of args provided")
    elif numargs == 1:
        stop = args[0]
    elif numargs == 2:
        (start, stop) = args
    elif numargs == 3:
        (start, stop, step) = args
    
    # generator
    # with yield each time you are calling this function will return a new value (next one)
    i = start
    while i <= stop:
        yield i;
        i += step
    


# Decorators => metadata
# we will need to return a function so we will define one in func1 (if we are not returning a function => it will be thrown an error)
def func1(f):
    def f2():
        print('before the call!')
        f()
        print('after the call')
    return f2
        

# basically func2 is given as argument for func1
@func1
def func2():
    print ('inside the function')


def ex(a, arr):
    a = 1
    arr[0] = 1

def main():
    f1(1,2,3)
    f1(1,2)
    f1(c=3,b=1,a=0)
    arr = [1,2,3]
    zeroes(arr)
    print(arr)
    arr = [1,2,3]
    not_zeroes(arr)
    print(arr) # [1,2,3]

    variable_args(1,2,3)
    variable_args()
    variable_args(1,2,3,4)
    my_list = [10,20,30,40]
    variable_args(*my_list)
    kargs(name="alex", age=23)
    
    my_details = {
        "name" : "alex",
        "age" : 23
    }
    
    kargs(**my_details)
    
    my_details = dict(name="alex", age=23)
    kargs(**my_details)
    
    
    res = sum(1,2,3,4,5,6)
    print(res)
    
    
    # generators example
    for i in inclusive_range(10):
        print(i)
    
    func2()
    
    a = 0
    arr = [0]
    ex(a,arr)
    print(a, arr) # 0, [1]


if __name__ == '__main__':
    main()
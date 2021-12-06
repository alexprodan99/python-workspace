# import random
# print(map.__doc__)
# print(random.__doc__)

def myFunction(arg1, arg2=None):
    """ myFunction(arg1, arg2=None) --> Doesn't really do anything, just prints.
    
    Parameters:
    arg1: the first argument
    arg2: second argument. Defaults to None.
    """
    print(arg1, arg2)


def main():
    print(myFunction.__doc__) # None if doc string is not defined

if __name__ == '__main__':
    main()
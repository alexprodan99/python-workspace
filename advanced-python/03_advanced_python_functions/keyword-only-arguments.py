
# you can have just 2 positional arguments then you will have just keyword arguments
def myFunction(arg1, arg2, *, supressExceptions=False):
    print(arg1, arg2, supressExceptions)


def main():
    myFunction(1,2)
    myFunction(1,2, supressExceptions=True)
if __name__ == '__main__':
    main()
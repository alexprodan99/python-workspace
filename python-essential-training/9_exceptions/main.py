import sys

def divide(a: int, b: int):
    if b == 0:
        raise ZeroDivisionError('Second argument cannot be 0')
    return a / b
def main():
    try:
        x = int('foo')
    except ValueError:
        print('ValueError')

    
    try:
        x = 2 / 0
    except ZeroDivisionError:
        print(f'Divide by zero exception {sys.exc_info()[1]}')
    else:
        # printed just if there is not an error
        print('Good job!')
        
    try:
        x = 2 / 0
    except ZeroDivisionError as e:
        print(e) # same as sys.exc_info()[1]
    
    try:
        divide(2,0)
    except ZeroDivisionError as e:
        print(e) # Second argument cannot be 0
        
    
    
    

if __name__ == '__main__':
    main()


def filterFunc(x):
    return x % 2 != 0

def filterFunc2(x):
    return x.islower()

def squareFunc(x):
    return x ** 2

def toGrade(x):
    if x >= 90:
        return "A"
    elif x >= 80 and x < 90:
        return "B"
    elif x >= 70 and x < 80:
        return "C"
    else:
        return "D"

def main():
    nums= [1,2,3,3,45,6,7]
    chars= 'abcdeeqAAAsdsa'
    grades= [123,123,1,4,2,412]
    
    odds = list(filter(filterFunc, nums))
    print(odds)
    odds = list(filter(lambda x: x % 2 != 0, nums))
    print(odds)
    
    lowers = list(filter(filterFunc2, chars))
    print(lowers)
    lowers = list(filter(lambda x: x.islower(), chars))
    print(lowers)
    
    squares = list(map(squareFunc, nums))
    print(squares)
    
    grades = sorted(grades)
    letters = list(map(toGrade, grades))
    print(letters)
    

if __name__ == '__main__':
    main()

import itertools

def testFunction(x):
    return x < 40


def main():
    seq1 = ["Joe", "John", "Mike"]
    vals = [10,20,30,40,50,40,30]
    
    # create a cycle
    cycle1 = itertools.cycle(seq1)
    
    print(next(cycle1))
    print(next(cycle1))
    print(next(cycle1))
    print(next(cycle1))
    
    # each time next is called a new value is generated with a step of 10
    count = itertools.count(100, 10)
    print(next(count)) # 100
    print(next(count)) # 110
    print(next(count)) # 120
    print(next(count)) # 130
    print(next(count))
    print(next(count))
    print(next(count))
    print(next(count))
    print(next(count))
    
    # by default will take vals[i-1] + vals[i] for generating current element
    acc = itertools.accumulate(vals)
    print(list(acc))
    
    # max(vals[i-1], vals[i])
    acc = itertools.accumulate(vals, max)
    print(list(acc))
    
    x = itertools.chain("ABCD", "1234")
    print(list(x)) # ['A', 'B', 'C', 'D', '1', '2', '3', '4']
    # a certain condition is met that stops them
    print(list(itertools.dropwhile(testFunction, vals))) # [40, 50, 40, 30]
    print(list(itertools.takewhile(testFunction, vals))) # [10, 20, 30]
    
    
    
if __name__ == '__main__':
    main()
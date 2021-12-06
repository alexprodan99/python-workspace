def main():
    days = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
    days2 = ['Dim', 'Lun', 'Mar', 'Mer', 'Jeu', 'Ven', 'Sam']
    
    i = iter(days)
    
    print(next(i))
    print(next(i))
    print(next(i))
    print(next(i))
    print(next(i))
    print(next(i))
    print(next(i))
    # if you are trying more than len of the list to call next() => StopIteration
    # print(next(i))
    
    with open('testfile.txt', 'r') as fp:
        # second param is the sentinel => character that you are looking for to stop iterations
        for line in iter(fp.readline, ''):
            print(line)
    # same results with readlines()
    with open('testfile.txt', 'r') as fp:
        for line in fp.readlines():
            print(line)
            
    for m in days:
        print(m)
    for i,v in enumerate(days):
        print(f'{i+1} - {v}')
    # another way (for not using i+1)
    for i,v in enumerate(days, start=1):
        print(f'{i} - {v}')
    
    # zip will return tuples (it will iterate through each collection in parallel)
    # what happens when collections are not of the same size ? => zip will terminate when the shortest collection index is reached
    # ('Sun', 'Dim')
    # ('Mon', 'Lun')
    # ('Tue', 'Mar')
    # ('Wed', 'Mer')
    # ('Thu', 'Jeu')
    # ('Fri', 'Ven')
    # ('Sat', 'Sam')
    for m in zip(days, days2):
        print(m)
    
    my_dict = dict(zip(days, days2))
    print(my_dict)
    
    for i, m in enumerate(zip(days, days2), start=1):
        print(i, m[0], '=', m[1], 'in French')

if __name__ == '__main__':
    main()
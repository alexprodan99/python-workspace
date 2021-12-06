# for advanced collections
import collections
import string

def main():
    # 1) named tuple
    Point = collections.namedtuple("Point",  "x y")
    p1 = Point(10,20)
    p2 = Point(30,40)
    print(p1, p2)
    print(p1.x, p1.y)
    # error
    # p1.x = 100
    p1 = p1._replace(x=100)
    print(p1.x)
    
    # 2) default dict
    # default values will be 0
    my_dict = collections.defaultdict(int)

    keys = ['aaa', 'bbb', 'aaa']
    
    for key in keys:
        my_dict[key] += 1
    
    for k,v in my_dict.items():
        print(k,v)
    
    # initial value is 100    
    my_dict = collections.defaultdict(lambda: 100)
    for key in keys:
        my_dict[key] += 1
    
    for k,v in my_dict.items():
        print(k,v)
    
    
    # 3) counters
    nums = [1,2,3,4,2,1,2,4]
    nums2 = [1,2,3]
    c1 = collections.Counter(nums)
    
    print(c1)
    print(c1[2]) # 3
    
    # list of tuples
    # [(2, 3), (1, 2), (4, 2), (3, 1)]
    print(c1.most_common())
    # first 3 most common
    print(c1.most_common(3))

    print(sum(c1.values()))
    print(sum(c1.keys()))
    
    # combine
    c1.update(nums2)
    print(c1)
    
    # substract
    c1.subtract(nums2)
    print(c1)
    
    
    # common elements between two counters
    
    c2 = collections.Counter(nums2)
    # {1: 1, 2: 1, 3: 1} => so 1,2,3 are common to both classes
    print ('common=', c1 & c2)
    
    
    
    # 4) ordereddict
    sport_teams = [('A', (100,20)), ('B', (122, 30)), ('C', (123,23))]
    
    sorted_teams = sorted(sport_teams, key=lambda x: x[1][0], reverse=True)
    # if you modify this collection then it will not automatically change to a sorted version, but you can pop elements
    teams = collections.OrderedDict(sorted_teams)
    
    print(teams)
    tm, wl = teams.popitem()
    print(tm, wl)
    
    for i,team in enumerate(teams, start=1):
        print(i, team)
    
    a = collections.OrderedDict({'a': 1, 'b': 2, 'c':3})
    b = collections.OrderedDict({'a': 1, 'b': 2, 'c':3})
    print(a == b) # True
    
    # if i change order or counting => False
    a = collections.OrderedDict({'a': 1, 'b': 2, 'c':3})
    b = collections.OrderedDict({'b': 2, 'a': 1,'c':3})
    print(a == b) # False
    
    
    a = collections.OrderedDict({'a': 1, 'b': 2, 'c':3})
    # b is just a regular dict
    b = {'b': 2, 'a': 1,'c':3}
    print(a == b) # True
    
    
    # 5) Deque
    d = collections.deque(string.ascii_lowercase)
    print('item count=', len(d))
    
    for element in d:
        print(element, end=",")
    
    d.pop()
    d.popleft()
    d.append(2)
    d.appendleft(1)
    print(d)
    
    
    # positive => right, negative => left
    # default = 1
    d.rotate()
    print(d)
    d.rotate(10)
    print(d)
    d.rotate(-11)
    print(d)
    
if __name__ == '__main__':
    main()    
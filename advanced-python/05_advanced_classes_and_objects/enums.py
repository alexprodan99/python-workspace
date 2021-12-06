
from enum import Enum, unique, auto

@unique
class Fruit(Enum):
    APPLE = 1
    BANANA = 2
    ORANGE = 3
    # if you don't care what value to put you can use auto => basically it will get last value used + 1 (if auto is for first item it will be 0 + 1 = 1)
    PEAR = auto()


def main():
    print(Fruit.APPLE) # Fruit.APPLE
    print(type(Fruit.APPLE)) # <enum 'Fruit'>
    print(repr(Fruit.APPLE)) # <Fruit.APPLE: 1>
    
    print(Fruit.APPLE.name) # APPLE
    print(Fruit.APPLE.value) # 1
    # you cannot have duplicate keys in Fruits (you can have duplicate values if you are not having unique decorator!)
    print(Fruit.PEAR.name) # PEAR
    print(Fruit.PEAR.value) # 4

if __name__ == '__main__':
    main()

from enum import Enum, unique

@unique
class Fruit(Enum):
    APPLE = 1
    BANANA = 2
    ORANGE = 3


def main():
    print(Fruit.APPLE) # Fruit.APPLE
    print(type(Fruit.APPLE)) # <enum 'Fruit'>
    print(repr(Fruit.APPLE)) # <Fruit.APPLE: 1>
    
    print(Fruit.APPLE.name) # APPLE
    print(Fruit.APPLE.value) # 1
    # you cannot have duplicate keys in Fruits (you can have duplicate values if you are not having unique decorator!)
    

if __name__ == '__main__':
    main()
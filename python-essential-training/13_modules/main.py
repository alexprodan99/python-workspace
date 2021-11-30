import sys
import os
import random
import datetime
import my_module
from my_module import sum
def main():
    v = sys.version_info
    print('Python version {}.{}.{}'.format(*v))
    print('OS={}'.format(os.name)) #nt
    print('PATH={}'.format(os.getenv('PATH')))
    print('current_dir={}'.format(os.getcwd()))
    print('25 random bytes from os={}'.format(os.urandom(25)))
    print('25 random bytes from os to hex={}'.format(os.urandom(25).hex()))
    print('a random int={}'.format(random.randint(1,1000)))
    my_list = list(range(25))
    random.shuffle(my_list)
    print('shuffle a list={}'.format(my_list))
    now = datetime.datetime.now()
    print('now={} year={} month={} day={}'.format(now, now.year, now.month, now.day))
    
    
    print('sum={}'.format(my_module.sum(1,2,3)))
    print('sum={}'.format(sum(1,2,3)))
    
if __name__ == '__main__':
    main()
class inclusive_range:
    def __init__(self, *args):
        numargs = len(args)
        self._start = 0
        self._step = 1
        
        if numargs < 1 or numargs > 3:
            raise TypeError('Incorrect number of argumets!')
        elif numargs == 1:
            self._stop = args[0]
        elif numargs == 2:
            (self._start, self._stop) = args
        elif numargs == 3:
            (self._start, self._stop, self._step) = args
        self._next = self._start
    def __iter__(self):
        return self
    
    def __next__(self):
        if (self._next > self._stop):
            raise StopIteration
        else:
            _r = self._next
            self._next += self._step
            return _r
        
def main():
    for n in inclusive_range(25):
        print(n, end=" ")

if __name__ == '__main__':
    main()
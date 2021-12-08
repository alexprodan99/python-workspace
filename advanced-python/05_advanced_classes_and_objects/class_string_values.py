class Person:
    def __init__(self):
        self.fname = 'Alex'
        self.lname = 'Prodan'
        self.age = 25
    
    def __repr__(self):
        return f'Person(fname={self.fname}, lname={self.lname}, age={self.age})'
    def __str__(self):
        return f'{self.fname} {self.lname} {self.age}'
    def __bytes__(self):
        val = 'Person(fname={self.fname}, lname={self.lname}, age={self.age})'
        return bytes(val.encode('utf-8'))

person = Person()
print(person) # Alex Prodan 25
print(repr(person))
print(str(person))
print(bytes(person)) # b'Person(fname={self.fname}, lname={self.lname}, age={self.age})'
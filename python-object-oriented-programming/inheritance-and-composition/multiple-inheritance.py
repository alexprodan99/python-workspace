class A:
    def __init__(self):
        super().__init__()
        self.foo = "foo"
        self.name = "class a"
    def func(self):
        print('class a')
class B:
    def __init__(self):
        super().__init__()
        self.bar = "bar"
        self.name = "class b"
    def func(self):
        print('class b')
class C(A,B):
    def __init__(self):
        super().__init__()
    def show_props(self):
        print(self.foo)
        print(self.bar)
        print(self.name) # class a => is looking in each of it's superclass and A is first in the list
    def call_func(self):
        self.func()
        
c = C()

c.show_props() # class a
c.call_func() # class a

# why class a ?
# method resolution order (C -> A -> B -> object)
print(C.__mro__)

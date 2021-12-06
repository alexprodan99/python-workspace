from dataclasses import dataclass

@dataclass(frozen=True)
class ImmutableClass:
    value1: str = "Value1"
    # you don't need explicitely to define field type if it has a default value
    value2 = 0
    
    
    def change_func(self, new_value):
        self.value2 = new_value

obj = ImmutableClass()
# error
# obj.value1 = '312'
print(obj.value1)

# error
# obj.change_func('312')
print(obj.value1)

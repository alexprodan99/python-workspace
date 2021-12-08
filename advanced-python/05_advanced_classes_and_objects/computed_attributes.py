class MyColor():
    def __init__(self):
        self.red = 50
        self.green = 75
        self.blue = 100

    # called when cannot found a value
    def __getattr__(self, attr):
        if attr == 'rgbcolor':
            return (self.red, self.green, self.blue)
        elif attr == 'hexcolor':
            return '#{0:02x}{1:02x}{2:02x}'.format(self.red, self.green, self.blue)
        else:
            raise AttributeError("Invalid attribute")
    
    def __setattr__(self, attr, val):
        if attr == 'rgbcolor':
            self.red = val[0]
            self.green = val[1]
            self.blue = val[2]
        # if is not an if case call super()..
        super().__setattr__(attr, val)
        
    # use dir to display available properties
    def __dir__(self):
        return ("red", "green", "blue", "rgbcolor", "hexcolor")
    
    

color = MyColor()
print(color.rgbcolor)
print(color.hexcolor)

color.rgbcolor = (255,0,0)
print(color.red)

print(dir(color)) # ['blue', 'green', 'hexcolor', 'red', 'rgbcolor']
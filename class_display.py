class Pixel(object):
    def __init__(self, r, g, b):
        if type(r) != int \
            or type(g) != int \
            or type(b) != int:
            raise TypeError("Only int numbers are allowed")

        for i in [r,g,b]:
            if not self.__class__.check_range(i):
                raise ValueError("Value should be in range 0..255")

        self.red = r
        self.blue = b
        self.green = g
       
    @staticmethod
    def check_range(val):
        if val >255 or val <0:
            return False
        return True

    @classmethod
    def add_new_val(cls, val):
        cls.newval = val

    def __str__(self):
        return "r: {:>3} g: {:>3} b: {:>3}".format(self.red, self.green, self.blue)

    def __add__(self, right):
        # self + righy -> self.__add__(right)
        if isinstance(right, self.__class__):
            return Pixel(self.red + right.red, self.green + right.green, self.blue + right.blue )
        elif type(right) == int:
            return Pixel(self.red + right, self.green + right, self.blue + right)
        raise TypeError('wrong type')

    def __radd__(self, left):
        #  left + self -> self.__radd__(left)
        #  self + left -> left.__radd__(self)
        return self + left

class Display(object):
    def __init__(self, w, h):
        if type(w) != int \
            or type(h) != int:
            raise TypeError("Only int numbers are allowed")
        
        if w < 0 or h < 0:
            raise ValueError("Value should be more then 0")
    
        self.width = w
        self.hight = h
    
        self.matrix = []
        for i in range(h):
            line = []
            for j in range(w):
                line.append(Pixel(0,0,0))
            self.matrix.append(line)




a = Pixel(12, 48, 154)
b = Pixel(46, 54, 15)

print(dir(a))
Pixel.add_new_val(5)
print(dir(a))


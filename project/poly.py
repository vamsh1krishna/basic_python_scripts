import math
class Rectangle():

    def __init__(self,width=None,height=None):
        self.width=width
        self.height=height
        #print(self.width,self.height)

    def __str__(self):
        #print(str(self))
        return "Rectangle(width="+str(self.width)+", "+"height="+str(self.height)+")"

    def set_width(self,width):
        self.width = width
        #print(self.width)

    def set_height(self,height):
        self.height = height
        #print(self.height)

    def get_area(self):
        area = self.width*self.height
        return area

    def get_perimeter(self):
        Perimeter = 2*self.width + 2*self.height
        return Perimeter

    def get_diagonal(self):
        diagonal = (self.width**2+self.height**2)**0.5
        return diagonal

    def get_picture(self):
        if self.width>50 or self.height>50:
            return "Too big for picture."
        else:
            pict = ("*"*self.width+ "\n")*self.height
            return pict

    def get_amount_inside(self,other):
        #print(self.get_area,other.get_area)
        K=self.get_area()/other.get_area()
        K=math.floor(K)
        return K

class Square(Rectangle):
    def __init__(self, width=None, height=None):
        self.width=width
        self.height=width
    def set_side(self,a):
        self.width=a
        self.height=a
        #print(self.width)
    def __str__(self):
        return "Square(side="+str(self.width)+")"
   



R=Rectangle()
R.set_width(3)
R.set_height(6)
R2=Rectangle(2,3)
print(R.get_area(),R2.get_area(),R2.get_amount_inside(R))
#print(R.get_perimeter())
#print(R.get_picture())
"""S=Square()
S.set_side(2)
print(S.get_area())
print(S.get_picture())
print(S.get_amount_inside(R))
print(S)"""






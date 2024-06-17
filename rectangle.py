class Rectangle():
    def __init__(self,len,bre):
        self.len=len
        self.bre=bre
    def Area(self):
        print("Area of rectangle :",self.len*self.bre)
    def peri(self):
        print("peri",2*(self.bre+self.len))

soo=Rectangle(4,5)
soo.Area()
soo.peri()
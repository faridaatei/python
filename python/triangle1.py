class Triangle:
  base = 0
  height = 0
  hypotunous=0
  def ____(self,base,height):
    self.base = base
    self.height=height
    self.hypotunous=hypotunous
  def area(self):
    return  0.5*self.base*self.height
      
  def perimeter(self):
    return 2*(self.base +self.height+hypotunous)
small = Triangle(20,30)
large=Triangle(600000,7000)
print("base and height of smaller {} and {}".format(small.base,small.height))
print("smaller area",small.area())
print("larger area",large.area())
        
        
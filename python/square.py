class Rectangle:
  length = 0
  width = 0
  
  def __init__(self,length,width):
    self.length = length
    self.width=width
    
  def area(self):
    return self.base*self.height
      
  def perimeter(self):
    return (self.base +self.height+hypotynous)
small = Rectangle(2,3)
large=Rectangle(5000,7000)
print("length and width of smaller {} and {}".format(small.length,small.width))
print("smaller area",small.area())
print("larger area",large.area())
        
        
class Rectangle:
  def __init__(self,width,height):
    self.width = width
    self.height = height
  
  def __str__(self):
    return f'Rectangle(width={self.width}, height={self.height})'
  
    #width getter
  def set_width(self, width):
    self.width=width
    
    #height setter
  def set_height(self, height):
    self.height=height
    
    # Area getter
  def get_area(self):
    return self.width * self.height
    
    # perimeter getter
  def get_perimeter(self):
    return 2 * self.width + 2 * self.height
    
    # diagonal getter
  def get_diagonal(self):
    return ((self.width **2 + self.height **2 )**.5)
   
    #visual display of the shape 
  def get_picture(self):
    if(self.width > 50 or self.height > 50):
      return "Too big for picture."
    string = (("*" * self.width)+ "\n")*self.height
    return string
    
    #getting values of a number
  def get_amount_inside(self,shape):
    return int(self.get_area() / shape.get_area())
    


  #the Square class that inherits from the Rectangle class
class Square(Rectangle):
  def __init__(self,side):
    self.width = side
    self.height = side
    
  def __str__(self):
    return f'Square(side={self.width})'
    
  def set_side(self,side):
    self.width = side
    self.height = side

  

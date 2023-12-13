class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def __str__(self):
        string ='Rectangle(width=' + str(self.width)+ ', height='+ str(self.height)+')'
        return string
    
    def set_width(self, width):
        self.width = width
    
    def set_height(self, height):
        self.height = height
    
    def get_area(self):
        area = self.width*self.height
        return area
    
    def get_perimeter(self):
        perimeter = 2 * self.width + 2 * self.height
        return perimeter
    
    def get_diagonal(self):
        diagonal = (self.width ** 2 + self.height ** 2) ** .5
        return diagonal
    
    def get_picture(self):
        picture = ''
        if self.width >50 or self.height>50:
            picture += 'Too big for picture.'
        else:
            for i in range(self.height):
                picture += '*'*self.width +'\n'
        
        return picture
    
    def get_amount_inside(self, shape):
        width_times = self.width // shape.width
        height_times = self.height // shape.height
        fit_times = width_times*height_times
        
        return fit_times

class Square(Rectangle):
    def __init__(self, length):
        self.height = length
        self.width = length
    
    def __str__(self):
        string ='Square(side=' + str(self.width)+ ')'
        return string
    
    def set_side (self, length):
        self.height = length
        self.width = length
    
    def set_width(self, width):
        self.width = width
        self.height = width
    
    def set_height(self, height):
        self.height = height
        self.width = height
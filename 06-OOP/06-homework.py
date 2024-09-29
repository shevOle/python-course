from math import pi

class Line:
    coordinates = {}

    def __init__(self, coordinate1, coordinate2):
        self.coordinates['x1'], self.coordinates['y1'] = coordinate1
        self.coordinates['x2'], self.coordinates['y2'] = coordinate2

    def get_coordinate_diff(self):
        x_diff = self.coordinates['x2'] - self.coordinates['x1']
        y_diff = self.coordinates['y2'] - self.coordinates['y1']
        return (x_diff, y_diff)

    def distance(self):
        x_diff, y_diff = self.get_coordinate_diff()
        return (x_diff ** 2 + y_diff ** 2) ** .5
    
    def slope(self):
        x_diff, y_diff = self.get_coordinate_diff()
        return y_diff / x_diff
    
new_line = Line((3,2), (8,10))
print(new_line.distance())
print(new_line.slope())
print()


class Cylinder:
    def __init__(self, height=1, radius=1):
        self.height = height
        self.radius = radius
    
    def volume(self):
        return pi * self.radius ** 2 * self.height
    
    def surface_area(self):
        return (2 * pi * self.radius * self.height) + (2 * pi * self.radius ** 2)
    
new_cylinder = Cylinder(2,3)
print(new_cylinder.volume())
print(new_cylinder.surface_area())
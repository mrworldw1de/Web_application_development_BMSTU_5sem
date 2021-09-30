from lab_python_oop.figure import Figure
from lab_python_oop.color import FigureColor
import math

class Circle(Figure):

    name = "Круг"

    @classmethod
    def get_figure_type(cls):
        return cls.name

    def __init__(self, c, r):
      
        self.r = r
        self.fc = FigureColor()
        self.fc.colorproperty = c

    def square(self):
      
        return math.pi*(self.r**2)

    def __repr__(self):
        return '\nНазвание фигуры: {}\nРадиус фигуры: {}\nПлощадь фигуры: {}\nЦвет фигуры: {}'.format(
            Circle.get_figure_type(),
            self.r,
            self.square(),
            self.fc.colorproperty
        )
from lab_python_oop.figure import Figure
from lab_python_oop.color import FigureColor

class Rectangle(Figure):
 
    name = "Прямоугольник"

    @classmethod
    def get_figure_type(cls):
        return cls.name

    def __init__(self, c, w, h):
        self.width = w
        self.height = h
        self.fc = FigureColor()
        self.fc.colorproperty = c

    def square(self):
        return self.width*self.height

    def __repr__(self):
        return '\nНазвание фигуры: {}\nШирина фигуры: {}\nВысота фигуры: {}\nПлощадь фигуры: {}\nЦвет фигуры: {}'.format(
            Rectangle.get_figure_type(),
            self.width,
            self.height,
            self.square(),
            self.fc.colorproperty
        )
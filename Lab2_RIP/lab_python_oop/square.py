from lab_python_oop.rectangle import Rectangle

class Square(Rectangle):
   
    name = "Квадрат"

    @classmethod
    def get_figure_type(cls):
        return cls.name

    def __init__(self, c, s):
        self.side = s
        super().__init__(c, self.side, self.side)

    def __repr__(self):
        return '\nНазвание фигуры: {}\nСторона фигуры: {}\nПлощадь фигуры: {}\nЦвет фигуры: {}'.format(
            Square.get_figure_type(),
            self.side,
            self.square(),
            self.fc.colorproperty
        )
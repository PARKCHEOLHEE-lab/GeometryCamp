from tkinter import *


class Rectangle:
    def __init__(self, x0, y0, x1, y1):
        super().__init__()
        self._x0 = x0
        self._y0 = y0
        self._x1 = x0
        self._y1 = y1
        self._x2 = x1
        self._y2 = y0
        self._x3 = x1
        self._y3 = y1
        self._width = abs(x0 - x1)
        self._height = abs(y0 - y1)
        self._rec_points = [self._x0,self._y0, self._x1,self._y1, self._x2,self._y2, self._x3,self._y3]
    
    def rec_coord(self):
        return self._x0, self._y0, self._x3, self._y3
    
    def rec_coord_all(self):
        return self._rec_points

    def rec_area(self):
        return self._width * self._height

    def rec_perimeter(self):
        return (self._width + self._height) * 2



class Window:
    def __init__(self):
        self._window = Tk()
        self._window.geometry("800x400")
        self.canvas = Canvas(self._window, width=550, height=400)

    def execute(self):
        return self._window.mainloop()



class Run:

    def app():

        frame = Rectangle(2,2, 398,398)
        frame = frame.rec_coord()

        rec = Rectangle(5,5,200,200)
        rec = rec.rec_coord()

        window = Window()
        window.canvas.create_rectangle(frame)
        window.canvas.grid(row=1, column=3)

        

        window.canvas.create_rectangle(rec)
        window.canvas.grid(row=2, column=3)

        window.execute()
        pass


Run.app()
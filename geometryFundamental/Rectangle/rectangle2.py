from tkinter import *
from typing import ClassVar

class Rectangle:
    def generate():
        global points

        R = 3
        REC_WIDTH = 1
        fill = "black"
        outline = "black"
        get_x0 = int(x0.get()) 
        get_y0 = int(y0.get())
        get_x1 = int(x1.get())
        get_y1 = int(y0.get())
        get_x2 = int(x0.get())
        get_y2 = int(y1.get())
        get_x3 = int(x1.get())
        get_y3 = int(y1.get())

        points = [get_x0, get_y0, get_x1, get_y1, get_x2, get_y2, get_x3, get_y3]

        def generate_points(x, y):
            canvas.create_oval(x-R, y-R, x+R, y+R, fill=fill, outline=outline)
        
        for i in range(0, len(points), 2):
            generate_points(points[i], points[i+1])

        canvas.create_rectangle(get_x0, get_y0, get_x3, get_y3, width=REC_WIDTH)
        canvas.pack()

    def area():
        return

    def perimeter():
        return


class App:
    global canvas
    global x0, y0, x1, y1

    window = Tk()
    window.geometry("550x350")
    canvas = Canvas(window, width=500, height=300)

    x0 = Entry(window, width=5); x0.place(x=440, y=45)
    y0 = Entry(window, width=5); y0.place(x=490, y=45)
    x1 = Entry(window, width=5); x1.place(x=440, y=75)
    y1 = Entry(window, width=5); y1.place(x=490, y=75)

    


    gen_button = Button(window, text="Generate", width=11, height=3, font=('Consolas Bold', 10), command=Rectangle.generate)
    gen_button.place(x=440, y=110)

    window.mainloop()
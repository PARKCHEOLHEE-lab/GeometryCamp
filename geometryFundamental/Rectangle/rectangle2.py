from tkinter import *

class Rectangle:
    def generate():
        R = 3
        REC_WIDTH = 1
        fill = "black"
        outline = "black"
        get_x0 = float(x0.get()); get_y0 = float(y0.get())
        get_x1 = float(x1.get()); get_y1 = float(y0.get())
        get_x2 = float(x0.get()); get_y2 = float(y1.get())
        get_x3 = float(x1.get()); get_y3 = float(y1.get())

        def generate_points(x, y):
            canvas.create_oval(x-R, y-R, x+R, y+R, fill=fill, outline=outline)
        
        def generate_area():
            width = abs(float(x0.get()) - float(x1.get()))
            height = abs(float(y0.get()) - float(y1.get()))
            area = width * height
            return round(area, 2) 

        def generate_perimeter():
            width = abs(float(x0.get()) - float(x1.get()))
            height = abs(float(y0.get()) - float(y1.get()))
            perimeter = (width + height) * 2
            return round(perimeter, 2)


        points = [get_x0, get_y0, get_x1, get_y1, get_x2, get_y2, get_x3, get_y3]
        for i in range(0, len(points), 2):
            generate_points(points[i], points[i+1])

        canvas.create_rectangle(get_x0, get_y0, get_x3, get_y3, width=REC_WIDTH)
        canvas.pack()

        area_label_var.set(generate_area())
        perimeter_label_var.set(generate_perimeter())


class App:
    global canvas
    global x0, y0, x1, y1
    global area_label_var, perimeter_label_var

    window = Tk()
    window.geometry("550x350")
    canvas = Canvas(window, width=500, height=300)

    x0 = Entry(window, width=5); x0.place(x=440, y=45)
    y0 = Entry(window, width=5); y0.place(x=490, y=45)
    x1 = Entry(window, width=5); x1.place(x=440, y=75)
    y1 = Entry(window, width=5); y1.place(x=490, y=75)

    gen_button = Button(window, text="Generate", width=11, height=3, font=('Consolas Bold', 10), command=Rectangle.generate)
    gen_button.place(x=440, y=110)

    perimeter_label_var = DoubleVar()
    area_label_var = DoubleVar()

    perimeter_title = Label(window, text="Square Premiter ▼", font=('Consolas', 10)); perimeter_title.place(x=420, y=200)
    perimeter_label = Entry(window, width=12, textvariable=perimeter_label_var); perimeter_label.place(x=440, y=230)
    area_title = Label(window, text="Square Area ▼", font=('Consolas', 10)); area_title.place(x=435, y=260)
    area_label = Entry(window, width=12, textvariable=area_label_var); area_label.place(x=440, y=290)


    window.mainloop()

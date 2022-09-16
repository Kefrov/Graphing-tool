from tkinter import *
from math import *

win = Tk()


def create_canvas():
    global step, cp, n_units

    z, y = 0, 0
    for i in range(n_units):
        cp.append(canvas.create_line(z, 0, z, ch, fill='gray', dash=(4, 2)))
        cp.append(canvas.create_line(0, y, ch, y, fill='gray', dash=(4, 2)))
        z += step
        y += step
    cp.append(canvas.create_line(int(c_half) + 1, ch, int(c_half) + 1, 1, fill='white', arrow=LAST))
    cp.append(canvas.create_line(0, int(c_half) + 1, ch - 1, int(c_half) + 1, fill='white', arrow=LAST))



def draw(zoom):
    global pts, app, step, n_units

    if not zoom:
        if entry.get() != '':
            b_apply.configure(text='clear')
        if app != '':
            clear_entry()
            b_apply.configure(text='apply')

    app = entry.get()
    z1 = -n_units - 0.02777
    z2 = -n_units
    for i in range(-int(n_units / 0.02777), int(n_units / 0.02777)):
        z1 += 0.02777
        z2 += 0.02777
        try:
            y1 = eval(app.replace('z', f'({str(z1)})'))
            y2 = eval(app.replace('z', f'({str(z2)})'))
                
            if -n_units < y1 < n_units:
                pts.append(canvas.create_line(z1 * step + c_half, -(y1 * step) + c_half, 
                z2 * step + c_half, -(y2 * step) + c_half, fill='red', width=3))  
        except Exception:  
             pass


def clear_entry():
    global pts, point

    for i in pts:
        canvas.delete(i)

    entry.delete(0, 'end')
    z_input.delete(0, 'end')
    y_value.configure(text='')
    canvas.delete(point)
    app = ''
    pts = []
    

def calc():
    global app, point
    
    canvas.delete(point)

    try:
        z = z_input.get()
        y = round(eval(app.replace('z', f'({str(z)})')), 3)
        y_value.configure(text=str(int(y) if y == int(y) else y))
        point = canvas.create_oval(float(z) * step + c_half - 5, -(y * step) + c_half - 5, 
                float(z) * step + c_half + 5, -(y * step) + c_half + 5, 
                outline='green', fill='light green')
    except Exception:
        pass


def zoom(sign):
    global step, n_units, point, pts, cp

    canvas.delete(point)
    for i in pts:
        canvas.delete(i)

    if sign == '+' and n_units > 6:
        n_units -= 2
        step = ch / n_units
    elif sign == '-' and n_units < 36:
        n_units += 2
        step = ch / n_units

    for i in cp:
        canvas.delete(i)

    create_canvas()
    draw(True)
    calc()
    

ww = int(1600 / 1.5)
ch = int(1600 / 2.2) 
c_half = ch / 2
n_units = 18
step = ch / n_units

pts = []
cp = []
point = ''
app = ''

win.title('Graphing tool')
win.iconbitmap('grid.ico')
win.configure(bg='black')
win.resizable(width=False, height=False)
win.geometry(f'{ww}x{ch}')

canvas = Canvas(win, bg='black', height=ch, width=ch)
canvas.pack(side='right')

credit = Label(win, bg='black', fg='white', font=('Microsoft Himalaya', 25), text='- Made by Fares -')
credit.pack()

entry_text = Label(text='f(z) = ', font=('Microsoft Himalaya', 30), bg='black', fg='white')
entry = Entry(win, bg='black', fg='white', cursor='ibeam', font=('Microsoft Himalaya', 30), 
        width=16, borderwidth=0)
entry.place(relx=0.19, rely=0.2, anchor=CENTER)
entry_text.place(relx=0.06, rely=0.2, anchor=CENTER)

b_apply = Button(win, bg='black', fg='light green', cursor='hand2', text='apply', 
          font=('Microsoft Himalaya', 25), width=5, command=lambda: draw(False))
b_apply.place(relx=0.159, rely=0.3, anchor=CENTER)

z_input_text = Label(text='z = ', font=('Microsoft Himalaya', 30), bg='black', fg='white')
z_input = Entry(win, bg='black', fg='white', cursor='ibeam', font=('Microsoft Himalaya', 30), 
          width=16, borderwidth=0)
z_input.place(relx=0.18, rely=0.6, anchor=CENTER)
z_input_text.place(relx=0.06, rely=0.6, anchor=CENTER)

y_text = Label(text='y = ', font=('Microsoft Himalaya', 30), bg='black', fg='white')
y_value = Label(font=('Microsoft Himalaya', 30), bg='black', fg='white')
y_value.place(relx=0.08, rely=0.7, anchor='w')
y_text.place(relx=0.06, rely=0.7, anchor=CENTER)

b_calc = Button(win, bg='black', fg='light green', cursor='hand2', text='apply', 
         font=('Microsoft Himalaya', 25), width=5, command=lambda: calc())
b_calc.place(relx=0.159, rely=0.8, anchor=CENTER)

zoom_in = Button(win, bg='black', fg='light green', cursor='hand2', text='+',
          font=('Microsoft Himalaya', 25), width=4, command=lambda: zoom('+'))
zoom_in.place(relx=0.932, rely=0.9)

zoom_out = Button(win, bg='black', fg='light green', cursor='hand2', text='-',
          font=('Microsoft Himalaya', 25), width=4, command=lambda: zoom('-'))
zoom_out.place(relx=0.932, rely=0.8)

create_canvas()

win.mainloop()

from tkinter import *
from math import *

win = Tk()


def draw():
    global pts, stop_draw, app

    if entry.get() != '':
        b_apply.configure(text='clear')
    if app != '':
        clear_entry()
        b_apply.configure(text='apply')

    app = entry.get()
    for i in range(-int(c_half) + 1, int(c_half) + 1):
        x1 = i / step
        x2 = (i + 1) / step
        try:
            y1 = eval(app.replace('x', f'({str(x1)})'))
            y2 = eval(app.replace('x', f'({str(x2)})'))
                
            if -20 < y1 < 20 and not stop_draw:
                pts.append(canvas.create_line(i + c_half, -(y1 * step) + c_half, 
                i + 1 + c_half, -(y2 * step) + c_half, fill='red', width=3))
                win.after(10, canvas.update())   
        except Exception:  
             pass

        stop_draw = False


def clear_entry():
    global pts, stop_draw, point

    for i in pts:
        canvas.delete(i)

    stop_draw = True
    entry.delete(0, 'end')
    x_input.delete(0, 'end')
    y_value.configure(text='')
    canvas.delete(point)
    app = ''
    pts = []
    

def calc():
    global app, point
    
    canvas.delete(point)

    try:
        x = x_input.get()
        y = round(eval(app.replace('x', f'({str(x)})')), 3)
        y_value.configure(text=str(int(y) if y == int(y) else y))
        point = canvas.create_oval(float(x) * step + c_half - 5, -(y * step) + c_half - 5, 
                float(x) * step + c_half + 5, -(y * step) + c_half + 5, 
                outline='green', fill='light green')
    except Exception:
        pass
    

sw = win.winfo_screenwidth()
ww = int(sw / 1.5)
ch = int(sw / 2.2)
c_half = ch / 2
step = ch / 18

pts = []
stop_draw = False
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

entry_text = Label(text='f(x) = ', font=('Microsoft Himalaya', 30), bg='black', fg='white')
entry = Entry(win, bg='black', fg='white', cursor='ibeam', font=('Microsoft Himalaya', 30), 
        width=16, borderwidth=0)
entry.place(relx=0.19, rely=0.2, anchor= CENTER)
entry_text.place(relx=0.06, rely=0.2, anchor=CENTER)

b_apply = Button(win, bg='black', fg='white', cursor='hand2', text='apply', 
          font=('Microsoft Himalaya', 25), width=5, command=lambda: draw())
b_apply.place(relx=0.159, rely=0.3, anchor= CENTER)

x_input_text = Label(text='x = ', font=('Microsoft Himalaya', 30), bg='black', fg='white')
x_input = Entry(win, bg='black', fg='white', cursor='ibeam', font=('Microsoft Himalaya', 30), 
          width=16, borderwidth=0)
x_input.place(relx=0.18, rely=0.6, anchor= CENTER)
x_input_text.place(relx=0.06, rely=0.6, anchor= CENTER)

y_text = Label(text='y = ', font=('Microsoft Himalaya', 30), bg='black', fg='white')
y_value = Label(font=('Microsoft Himalaya', 30), bg='black', fg='white')
y_value.place(relx=0.08, rely=0.7, anchor='w')
y_text.place(relx=0.06, rely=0.7, anchor= CENTER)

b_calc = Button(win, bg='black', fg='white', cursor='hand2', text='apply', 
         font=('Microsoft Himalaya', 25), width=5, command=lambda: calc())
b_calc.place(relx=0.159, rely=0.8, anchor= CENTER)

x, y = 0, 0
for i in range(18):
    canvas.create_line(x, 0, x, ch, fill='gray', dash=(4, 2))
    canvas.create_line(0, y, ch, y, fill='gray', dash=(4, 2))
    x += step
    y += step
y_axis = canvas.create_line(int(c_half) + 1, ch, int(c_half) + 1, 1, fill='white', arrow=LAST)
x_axis = canvas.create_line(0, int(c_half) + 1, ch - 1, int(c_half) + 1, fill='white', arrow=LAST)

win.mainloop()

import tkinter as tk
from tkinter import ttk

def calc(n1, n2, op):
    if op == "+":
        ans = n1 + n2
    elif op == "-":
        ans = n1 - n2
    elif op == "*":
        ans = n1 * n2
    elif op == "/":
        ans = round(n1 / n2)
    elif op == "pow":
        ans = n1 ** n2

    return ans

def ccal (text, n1, n2, op):
    v1 = float(n1)
    v2 = float(n2)

    ans = calc(v1, v2, op)

    text.configure(text = "Resultado: " + str(ans))

def inv(text, n1, n2, op):
    v1 = float(n1)
    v2 = float(n2)

    ans = (calc(v1,v2,op))
    if ans == 0:
        ans = "ERROR"
    else:
        ans = round((1/ans),3)

    text.configure(text = "Inverso: " + str(ans))

def rt(text, n1, n2, op):
    v1 = float(n1)
    v2 = float(n2)

    ans = calc(v1,v2,op)

    if ans < 0:
        ans = "ERROR"
    else:
        ans = round((ans**0.5),3)

    text.configure(text = "Raiz cuadrada: " + str(ans))

def sq(text, n1, n2, op):
    v1 = float(n1)
    v2 = float(n2)

    ans = round((calc(v1,v2,op)**2), 3)

    text.configure(text = "Cuadrado: " + str(ans))

def ivent():
    vent = tk.Tk()
    vent.title("Calculadora de dos variables")
    vent.geometry("400x300")

    text = tk.Label(vent, text="Calculadora", font=("Pixel", 15))
    text.grid(column = 0, row = 0)

    lent1 = tk.Label(vent, text="Ingrese primer número", font=("Pixel", 10))
    lent1.grid(column = 0, row = 1)

    lent2 = tk.Label(vent, text="Ingrese segundo número", font=("Pixel", 10))
    lent2.grid(column=0, row=2)

    ent1 = tk.Entry(vent, width=10)
    ent2 = tk.Entry(vent, width=10)

    ent1.focus()
    ent2.focus()

    ent1.grid(column=1, row=1)
    ent2.grid(column=1, row=2)

    lop = tk.Label(vent, text="Operador: ", font=("Pixel", 15))
    lop.grid(column=0, row=3)

    ops = ttk.Combobox(vent)
    ops["values"]= ("+","-","*","/","pow")
    ops.current(0)
    ops.grid(column=1, row=3)

    lans = tk.Label(vent, text="Resultado: ", font=("Pixel", 15))
    lans.grid(column = 0, row = 9)

    linv = tk.Label(vent, text ="Inverso: ", font=("pixel, 15"))
    linv.grid(column=0,row=10)

    lrt = tk.Label(vent, text="Raíz cuadrada: ", font=("pixel, 15"))
    lrt.grid(column=0, row=11)

    lsq = tk.Label(vent, text="Cuadrado ", font=("pixel, 15"))
    lsq.grid(column=0, row=15)

    butt2 = tk.Button(vent,
                     command = lambda: inv(
                         linv,
                         ent1.get(),
                         ent2.get(),
                         ops.get()),
                     text="inverso",
                     bg="#cf0000",
                     fg="white")
    butt2.grid(column = 2, row = 5)

    butt = tk.Button(vent,
                     command=lambda: ccal(
                         lans,
                         ent1.get(),
                         ent2.get(),
                         ops.get()),
                     text="calcular",
                     bg="purple",
                     fg="white")
    butt.grid(column=1, row=5)

    butt3 = tk.Button(vent,
                     command=lambda: rt(
                         lrt,
                     ent1.get(),
                     ent2.get(),
                     ops.get()),
                     text="raíz",
                     bg="#0087ff",
                     fg="white")
    butt3.grid(column=2, row=6)

    butt4 = tk.Button(vent,
                      command=lambda: sq(
                          lsq,
                          ent1.get(),
                          ent2.get(),
                          ops.get()),
                      text="^2",
                      bg="#ec8800",
                      fg="white")
    butt4.grid(column=2, row=7)

    vent.mainloop()

def main():
    ivent()

main()

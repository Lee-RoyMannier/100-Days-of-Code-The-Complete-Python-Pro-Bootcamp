import tkinter as tk

screen = tk.Tk()
screen.title("Mile to km Converter")
screen.minsize(width=300, height=100)
screen.config(padx=20, pady=20)

# Creation Label
label = tk.Label(text="is equal to")
label.grid(column=0, row=1)

# creation Entry
entry_miles = tk.Entry(width=10)
entry_miles.grid(column=1, row=0)

# Creation Resulat label  and km/miles label

resul = tk.Label(text=0)
resul.grid(column=1, row=1)

mile_label = tk.Label(text="Miles")
mile_label.grid(column=2, row=0)

km_label = tk.Label(text="Km")
km_label.grid(column=2, row=1)

# Creation butn


def covert_mile_to_km():
    miles = float(entry_miles.get())
    miles = int(miles * 1.609)
    resul.config(text=miles)


btn = tk.Button(text="Calculate", command=covert_mile_to_km)
btn.grid(column=1, row=2)
screen.mainloop()

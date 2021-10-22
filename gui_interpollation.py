"""
Docstring

TODO
"""

import tkinter as tk

# Button callback
def calculate():
    x_1 = float(ent_ind_var_1.get())
    x_2 = float(ent_ind_var_2.get())
    x_i = float(ent_ind_var_i.get())
    y_1 = float(ent_de_var_1.get())
    y_2 = float(ent_de_var_2.get())
    # Linear interpollation formula
    y_i = y_1 + ((x_i - x_1) * (y_2 - y_1) / (x_2 - x_1))
    lbl_de_var_r["text"] = '{:.6f}'.format(y_i)


# Creating window
window = tk.Tk()

# Widgets
lbl_title = tk.Label(text="Linear Interpollation")
lbl_ind_var_1 = tk.Label(text="Independant variable 1")
lbl_ind_var_2 = tk.Label(text="Independant variable 2")
lbl_de_var_1 = tk.Label(text="Dependant variable 1")
lbl_de_var_i = tk.Label(text="Interpollated Value")
lbl_de_var_2 = tk.Label(text="Dependant variable 1")
lbl_ind_var_i = tk.Label(text="Intermediate variable")
ent_ind_var_i = tk.Entry()
ent_ind_var_1 = tk.Entry()
ent_ind_var_2 = tk.Entry()
ent_de_var_1 = tk.Entry()
lbl_de_var_r = tk.Label(text="No inputs yet!")
ent_de_var_2 = tk.Entry()
btn_calc = tk.Button(text="Interpollate!", command=calculate)

# Widget placement
lbl_title.grid(row=0, column=1)
lbl_ind_var_1.grid(row=1, column=0)
lbl_ind_var_i.grid(row=1, column=1)
lbl_ind_var_2.grid(row=1, column=2)
ent_ind_var_1.grid(row=2, column=0)
ent_ind_var_i.grid(row=2, column=1)
ent_ind_var_2.grid(row=2, column=2)
lbl_de_var_1.grid(row=3, column=0)
lbl_de_var_i.grid(row=3, column=1)
lbl_de_var_2.grid(row=3, column=2)
ent_de_var_1.grid(row=4, column=0)
lbl_de_var_r.grid(row=4, column=1)
ent_de_var_2.grid(row=4, column=2)
btn_calc.grid(row=5, column=1)

# Resizing handling
window.columnconfigure([0, 1, 2], weight=1, minsize=50)
window.rowconfigure([0, 1, 2, 3, 4, 5], weight=1, minsize=50)

window.mainloop()

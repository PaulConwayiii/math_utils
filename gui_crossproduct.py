"""
Docstring

TODO
"""

import tkinter as tk

# Button callback
def calculate():
    r_x = float(ent_r_x.get())
    r_y = float(ent_r_y.get())
    r_z = float(ent_r_z.get())
    v_x = float(ent_v_x.get())
    v_y = float(ent_v_y.get())
    v_z = float(ent_v_z.get())
    cross_x = (r_y * v_z) - (r_z * v_y)
    cross_y = (r_z * v_x) - (r_x * v_z)
    cross_z = (r_x * v_y) - (r_y * v_x)
    lbl_cross_x_res["text"] = '{:.6f}'.format(cross_x)
    lbl_cross_y_res["text"] = '{:.6f}'.format(cross_y)
    lbl_cross_z_res["text"] = '{:.6f}'.format(cross_z)
    """
    x_1 = float(ent_ind_var_1.get())
    x_2 = float(ent_ind_var_2.get())
    x_i = float(ent_ind_var_i.get())
    y_1 = float(ent_de_var_1.get())
    y_2 = float(ent_de_var_2.get())
    # Linear interpollation formula
    y_i = y_1 + ((x_i - x_1) * (y_2 - y_1) / (x_2 - x_1))
    lbl_de_var_r["text"] = '{:.6f}'.format(y_i)
    """


# Creating window
window = tk.Tk()

# Widgets
lbl_title = tk.Label(text="Cross Product Calculator")
lbl_vec_r = tk.Label(text="r=")
ent_r_x = tk.Entry()
lbl_r_x = tk.Label(text="i+")
ent_r_y = tk.Entry()
lbl_r_y = tk.Label(text="j+")
ent_r_z = tk.Entry()
lbl_r_z = tk.Label(text="k")
lbl_vec_v = tk.Label(text="v=")
ent_v_x = tk.Entry()
lbl_v_x = tk.Label(text="i+")
ent_v_y = tk.Entry()
lbl_v_y = tk.Label(text="j+")
ent_v_z = tk.Entry()
lbl_v_z = tk.Label(text="k")
btn_calc = tk.Button(text="rXv=", command=calculate)
lbl_cross_x_res = tk.Label(text="")
lbl_cross_x = tk.Label(text="i+")
lbl_cross_y_res = tk.Label(text="")
lbl_cross_y = tk.Label(text="j+")
lbl_cross_z_res = tk.Label(text="")
lbl_cross_z = tk.Label(text="k")


# Widget placement
lbl_title.grid(row=0, column=3)
lbl_vec_r.grid(row=1, column=0)
ent_r_x.grid(row=1, column=1)
lbl_r_x.grid(row=1, column=2)
ent_r_y.grid(row=1, column=3)
lbl_r_y.grid(row=1, column=4)
ent_r_z.grid(row=1, column=5)
lbl_r_z.grid(row=1, column=6)
lbl_vec_v.grid(row=2, column=0)
ent_v_x.grid(row=2, column=1)
lbl_v_x.grid(row=2, column=2)
ent_v_y.grid(row=2, column=3)
lbl_v_y.grid(row=2, column=4)
ent_v_z.grid(row=2, column=5)
lbl_v_z.grid(row=2, column=6)
btn_calc.grid(row=3, column=0)
lbl_cross_x_res.grid(row=3, column=1)
lbl_cross_x.grid(row=3, column=2)
lbl_cross_y_res.grid(row=3, column=3)
lbl_cross_y.grid(row=3, column=4)
lbl_cross_z_res.grid(row=3, column=5)
lbl_cross_z.grid(row=3, column=6)


# Resizing handling
window.columnconfigure([0, 1, 2], weight=1, minsize=50)
window.rowconfigure([0, 1, 2, 3, 4, 5], weight=1, minsize=50)

window.mainloop()

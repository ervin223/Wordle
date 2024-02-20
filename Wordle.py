from tkinter import *
import tkinter as tk

def send(file_path):
    sonastik = {}
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            if '-' in line:
                vene, eesti = line.strip().split('-')
                sonastik[vene] = eesti
            else:
                print(f"{line.strip()}")
    return sonastik

send("sonad2.txt")

class VirtualKeyboard:
    def __init__(self, master):
        self.master = master
        self.master.title("Virtual Keyboard")
        self.entry = tk.Entry(master)
        self.entry.pack()
        self.create_keyboard()

    def create_keyboard(self):
        buttons = [
            ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p'],
            ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l'],
            ['z', 'x', 'c', 'v', 'b', 'n', 'm']
        ]

        for row in buttons:
            row_frame = tk.Frame(self.master)
            row_frame.pack()
            for char in row:
                button = tk.Button(row_frame, text=char, width=4, command=lambda c=char: self.insert_char(c))
                button.pack(side=tk.LEFT)

    def insert_char(self, char):
        self.entry.insert(tk.END, char)

def main():
    root = tk.Tk()
    keyboard = VirtualKeyboard(root)
    root.mainloop()

if __name__ == "__main__":
    main()

root = tk.Tk()
root.geometry("400x500")
root.title("Quadratic Equation Solver")

label_b = tk.Label(root, font=("Arial", 14))
label_b.grid(row=1, column=1,padx=5, pady=5)
label_c = tk.Label(root, font=("Arial", 14))
label_c.grid(row=2, column=1,padx=5, pady=5)
label_d = tk.Label(root, font=("Arial", 14))
label_d.grid(row=3, column=1,padx=5, pady=5)
label_e = tk.Label(root, font=("Arial", 14))
label_e.grid(row=4, column=1,padx=5, pady=5)
label_f = tk.Label(root, text=" ", font=("Arial", 14))
label_f.grid(row=5, column=1,padx=5, pady=5)
label_g = tk.Label(root, text=" ", font=("Arial", 14))
label_g.grid(row=6, column=1,padx=5, pady=5)

label_ab = tk.Label(root, font=("Arial", 14))
label_ab.grid(row=1, column=1,padx=5, pady=5)
label_ac = tk.Label(root, text="2", font=("Arial", 14))
label_ac.grid(row=1, column=2,padx=5, pady=5)
label_ad = tk.Label(root, text="2", font=("Arial", 14))
label_ad.grid(row=1, column=3,padx=5, pady=5)
label_ae = tk.Label(root, text="2", font=("Arial", 14))
label_ae.grid(row=1, column=4,padx=5, pady=5)
label_af = tk.Label(root, text="2", font=("Arial", 14))
label_af.grid(row=1, column=5,padx=5, pady=5)
label_ag = tk.Label(root, text="2", font=("Arial", 14))
label_ag.grid(row=1, column=6,padx=5, pady=5)

label_bb = tk.Label(root, text="1", font=("Arial", 14))
label_bb.grid(row=2, column=1,padx=5, pady=5)
label_bc = tk.Label(root, text="2", font=("Arial", 14))
label_bc.grid(row=2, column=2,padx=5, pady=5)
label_bd = tk.Label(root, text="2", font=("Arial", 14))
label_bd.grid(row=2, column=3,padx=5, pady=5)
label_be = tk.Label(root, text="2", font=("Arial", 14))
label_be.grid(row=2, column=4,padx=5, pady=5)
label_bf = tk.Label(root, text="2", font=("Arial", 14))
label_bf.grid(row=2, column=5,padx=5, pady=5)
label_bg = tk.Label(root, text="2", font=("Arial", 14))
label_bg.grid(row=2, column=6,padx=5, pady=5)

label_eb = tk.Label(root, text="1", font=("Arial", 14))
label_eb.grid(row=3, column=1,padx=5, pady=5)
label_ec = tk.Label(root, text="2", font=("Arial", 14))
label_ec.grid(row=3, column=2,padx=5, pady=5)
label_ed = tk.Label(root, text="2", font=("Arial", 14))
label_ed.grid(row=3, column=3,padx=5, pady=5)
label_ee = tk.Label(root, text="2", font=("Arial", 14))
label_ee.grid(row=3, column=4,padx=5, pady=5)
label_ef = tk.Label(root, text="2", font=("Arial", 14))
label_ef.grid(row=3, column=5,padx=5, pady=5)
label_eg = tk.Label(root, text="2", font=("Arial", 14))
label_eg.grid(row=3, column=6,padx=5, pady=5)

label_db = tk.Label(root, text="1", font=("Arial", 14))
label_db.grid(row=4, column=1,padx=5, pady=5)
label_dc = tk.Label(root, text="2", font=("Arial", 14))
label_dc.grid(row=4, column=2,padx=5, pady=5)
label_dd = tk.Label(root, text="2", font=("Arial", 14))
label_dd.grid(row=4, column=3,padx=5, pady=5)
label_de = tk.Label(root, text="2", font=("Arial", 14))
label_de.grid(row=4, column=4,padx=5, pady=5)
label_df = tk.Label(root, text="2", font=("Arial", 14))
label_df.grid(row=4, column=5,padx=5, pady=5)
label_dg = tk.Label(root, text="2", font=("Arial", 14))
label_dg.grid(row=4, column=6,padx=5, pady=5)

label_fb = tk.Label(root, text="1", font=("Arial", 14))
label_fb.grid(row=5, column=1,padx=5, pady=5)
label_fc = tk.Label(root, text="2", font=("Arial", 14))
label_fc.grid(row=5, column=2,padx=5, pady=5)
label_fd = tk.Label(root, text="2", font=("Arial", 14))
label_fd.grid(row=5, column=3,padx=5, pady=5)
label_fe = tk.Label(root, text="2", font=("Arial", 14))
label_fe.grid(row=5, column=4,padx=5, pady=5)
label_ff = tk.Label(root, text="2", font=("Arial", 14))
label_ff.grid(row=5, column=5,padx=5, pady=5)
label_fg = tk.Label(root, text="2", font=("Arial", 14))
label_fg.grid(row=5, column=6,padx=5, pady=5)

label_hb = tk.Label(root, text="1", font=("Arial", 14))
label_hb.grid(row=6, column=1,padx=5, pady=5)
label_hc = tk.Label(root, text="2", font=("Arial", 14))
label_hc.grid(row=6, column=2,padx=5, pady=5)
label_hd = tk.Label(root, text="2", font=("Arial", 14))
label_hd.grid(row=6, column=3,padx=5, pady=5)
label_he = tk.Label(root, text="2", font=("Arial", 14))
label_he.grid(row=6, column=4,padx=5, pady=5)
label_hf = tk.Label(root, text="2", font=("Arial", 14))
label_hf.grid(row=6, column=5,padx=5, pady=5)
label_hg = tk.Label(root, text="2", font=("Arial", 14))
label_hg.grid(row=6, column=6,padx=5, pady=5)

root.mainloop()

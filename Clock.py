import tkinter as tk
import tkinter.ttk as ttk
import time

class Clock(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Relógio")
        self.geometry("800x500")
        self.minsize(700, 500)
        self.configure(bg="grey")

        # Adicionando estilo
        style = ttk.Style()
        style.configure("TFrame", background="grey", borderwidth=0, relief="raised")

        # Barra superior
        self.top_bar = ttk.Frame(self, style="TFrame", height=30)
        self.top_bar.pack(side=tk.TOP, fill=tk.X)
        
        self.top_bar.configure(style="TFrame.Horizontal.TFrame")

        # Botões à barra superior
        self.button1 = tk.Button(self.top_bar, text="Botão 1", bg="grey", fg="white", bd=0, relief=tk.FLAT)
        self.button1.pack(side=tk.LEFT, padx=10, pady=5)
        
        # Sombra à barra superior
        self.top_bar.bind("<Configure>", self.top_bar_shadow)

        self.label = tk.Label(self, font=("Helvetica", 60), bg="grey", fg="white", justify='center', anchor='center')
        self.label.place(relx=0.5, rely=0.5, anchor="center" )

        self.label2 = tk.Label(self, font=("Helvetica", 30), bg="grey", fg="white", justify='center', anchor='center')
        self.label2.place(relx=0.5, rely=0.6, anchor="center")

        self.update_clock()

    def update_clock(self):
        current_time = time.strftime("%I:%M:%S %p")
        current_day = time.strftime("%d/%m")
        self.label.configure(text=current_time)
        self.label2.configure(text="Dia " + current_day)
        self.after(1000, self.update_clock)
        
    def top_bar_shadow(self, event):
        x = self.winfo_rootx() + self.top_bar.winfo_x()
        y = self.winfo_rooty() + self.top_bar.winfo_y()
        width = self.top_bar.winfo_width()
        self.top_bar_shadow = ttk.Frame(self, height=5, style="TFrame.Horizontal.TFrame")
        self.top_bar_shadow.place(x=x, y=y+30, width=width)
        
if __name__ == "__main__":
    clock = Clock()
    clock.mainloop()

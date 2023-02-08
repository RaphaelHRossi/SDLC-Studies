import tkinter as tk
import time

class Clock(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Relógio")
        self.geometry("800x500")
        self.minsize(700, 500)
        self.configure(bg="grey")
        
        self.label = tk.Label(self, font=("Helvetica", 60), bg="grey", fg="white", justify='center', anchor='center')
        self.label.place(relx=0.5, rely=0.5, anchor="center" )
        
        self.update_clock()

    def update_clock(self):
        current_time = time.strftime("%I:%M:%S %p")
        self.label.configure(text=current_time)
        self.after(1000, self.update_clock)

if __name__ == "__main__":
    clock = Clock()
    clock.mainloop()

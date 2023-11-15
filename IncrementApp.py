import tkinter as tk
from tkinter import ttk

class App:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Counter App")
        self.root.iconbitmap("app.ico")
        self.root.geometry("300x100")
        self.count = 0
        self.label = ttk.Label(self.root, text=str(self.count))
        self.label.pack(pady=10)

        self.button = ttk.Button(self.root, text="Increment", command=self.increment_count)
        self.button.pack(pady=10)

        self.root.mainloop()

    def increment_count(self):
        self.count += 1
        self.label.config(text=str(self.count))

if __name__ == "__main__":
    app = App()
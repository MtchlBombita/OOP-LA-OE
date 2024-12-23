import tkinter as tk

name = "MITCHEL BOMBITA"
section = "BSIT-2ABC"
root = tk.Tk()
root.title("OOP")
root.geometry("1366x768")
root.configure(bg="Khaki")

frame = tk.Frame(root)
frame.pack(pady=200)

label = tk.Label(frame, text= (f"OOP LA29 {name}, {section}"))
label.grid(row=0, column=0, padx=200, pady=100)
root.mainloop()

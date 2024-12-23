import tkinter as tk 
name = "Bombita, Mitchel"
section = "BSIT-2B"
web_title = "OOP"
root = tk.Tk()
root.title(f"{web_title}")
root.geometry("500x300")
root.configure(bg="Gray")

label = tk.Label(root, text = (f"{web_title} LA29 {name} {section}"))
label.grid(row=0, column= 0)

def display_text():
    print(f"My favorite anime is Bleach")

button = tk.Button(root, text= "Click me fafa",command = display_text)
button.grid(row=2, column= 0)
    

root.mainloop()

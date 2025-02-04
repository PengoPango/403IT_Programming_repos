import tkinter as tk


#create main window
root =tk.Tk()
root.title("Simple Tkinter Window")
root.geometry("400x500") # set window size WxH
root.config(bg="orchid")

#create a label
label = tk.Label(root, text="Hello,Tkinter!", font=("Arial",14))
label.pack(pady=20)
label.config(bg="lavender", fg="indigo")

#ariable to track the toggle state
toggle = False

buttoncount = 0

#function to change the text when the button is clicked
def toggle_text():
    global toggle # use the global variable to track state
    if toggle:
        label.config(text="Button Clicked!")
    else:
        label.config(text="Clicked Button!")
    toggle = not toggle #flip the state
    
    
#create a button
button = tk.Button(root, text="Press Me", command=toggle_text,)
button.pack(pady=100)
button.config(bg="lavender", fg="indigo")


buttonreset = tk.Button(root, text="Reset", command=lambda: label.config(text="Tkinter,Hello!", bg="red", fg="orange") )
buttonreset.pack(pady=90)
buttonreset.config(bg="steel blue", fg="midnight blue")
#run the application
root.mainloop()


import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Button Example")

# Function to display a message
def show_message(message):
    label.config(text=message)

# Create a label to display messages
label = tk.Label(root, text="Click a button")
label.pack(pady=10)

# Create buttons and add them to the window
button1 = tk.Button(root, text="Button 1", command=lambda: show_message("Button 1 Clicked"))
button1.pack(pady=5)

button2 = tk.Button(root, text="Button 2", command=lambda: show_message("Button 2 Clicked"))
button2.pack(pady=5)

button3 = tk.Button(root, text="Button 3", command=lambda: show_message("Button 3 Clicked"))
button3.pack(pady=5)

# Run the application
root.mainloop()

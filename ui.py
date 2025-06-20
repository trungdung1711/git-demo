import tkinter as tk

# Initialize the main window
root = tk.Tk()
root.title("Click the button!")

# Initialize counter variable
count = 0

# Label to show the count
label = tk.Label(root, text="Count: 0", font=("Arial", 20))
label.pack(pady=10)

# Function to update the count
def increment_count():
    global count
    count += 1
    label.config(text=f"Count: {count}")

# Button to trigger counting
button = tk.Button(root, text="Click me!", font=("Arial", 16), command=increment_count)
button.pack(pady=10)

# Start the GUI loop
root.mainloop()

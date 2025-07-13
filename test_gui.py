import tkinter as tk

def test_gui():
    print("Creating test GUI...")
    root = tk.Tk()
    root.title("Test GUI")
    root.geometry("400x300")
    
    label = tk.Label(root, text="Hello! This is a test GUI.")
    label.pack(pady=20)
    
    button = tk.Button(root, text="Click me!", command=lambda: print("Button clicked!"))
    button.pack(pady=10)
    
    print("GUI created, starting mainloop...")
    root.mainloop()
    print("GUI closed")

if __name__ == "__main__":
    test_gui() 
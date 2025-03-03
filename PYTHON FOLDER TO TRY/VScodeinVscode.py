import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import subprocess
import os
import pygments
from pygments.lexers import PythonLexer
from pygments.formatters import TkinterFormatter

class SimpleCodeEditor:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Python Code Editor")
        self.root.geometry("800x600")
        
        # Create a Text widget to write code
        self.text_widget = tk.Text(root, wrap=tk.WORD, font=("Courier", 12))
        self.text_widget.pack(expand=True, fill=tk.BOTH)
        
        # Add a Scrollbar
        self.scrollbar = tk.Scrollbar(root, command=self.text_widget.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.text_widget.config(yscrollcommand=self.scrollbar.set)

        # Menu Bar
        self.menu_bar = tk.Menu(root)
        root.config(menu=self.menu_bar)
        
        # File Menu
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)
        self.file_menu.add_command(label="Open", command=self.open_file)
        self.file_menu.add_command(label="Save", command=self.save_file)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=root.quit)
        
        # Run Menu
        self.run_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Run", menu=self.run_menu)
        self.run_menu.add_command(label="Run Script", command=self.run_script)
        
        # Syntax Highlighting
        self.text_widget.bind("<KeyRelease>", self.apply_syntax_highlighting)

    def open_file(self):
        file_path = filedialog.askopenfilename(defaultextension=".py", filetypes=[("Python files", "*.py"), ("All files", "*.*")])
        if file_path:
            with open(file_path, 'r') as file:
                code = file.read()
            self.text_widget.delete(1.0, tk.END)
            self.text_widget.insert(tk.END, code)
            self.apply_syntax_highlighting()  # Apply syntax highlighting after opening a file

    def save_file(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".py", filetypes=[("Python files", "*.py"), ("All files", "*.*")])
        if file_path:
            with open(file_path, 'w') as file:
                code = self.text_widget.get(1.0, tk.END)
                file.write(code)
            messagebox.showinfo("Save", "File saved successfully!")

    def run_script(self):
        code = self.text_widget.get(1.0, tk.END)
        try:
            exec(code)  # Executes the script in the same environment
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

    def apply_syntax_highlighting(self, event=None):
        code = self.text_widget.get(1.0, tk.END)
        formatter = TkinterFormatter()
        highlighted_code = pygments.highlight(code, PythonLexer(), formatter)
        self.text_widget.delete(1.0, tk.END)
        self.text_widget.insert(tk.END, highlighted_code)

# Create the main window
root = tk.Tk()

# Create the editor instance
editor = SimpleCodeEditor(root)

# Run the Tkinter main loop
root.mainloop()

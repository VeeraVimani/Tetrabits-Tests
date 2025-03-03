import tkinter as tk

class Block:
    def __init__(self, canvas, x, y, text):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.text = text
        
        self.rect = canvas.create_rectangle(x, y, x + 100, y + 50, fill="lightblue", outline="black")
        self.label = canvas.create_text(x + 50, y + 25, text=text)
        
        self.canvas.tag_bind(self.rect, "<Button-1>", self.on_click)
        self.canvas.tag_bind(self.rect, "<B1-Motion>", self.on_drag)
        
        self.offset_x = 0
        self.offset_y = 0
        
    def on_click(self, event):
        self.offset_x = event.x - self.x
        self.offset_y = event.y - self.y
        
    def on_drag(self, event):
        self.x = event.x - self.offset_x
        self.y = event.y - self.offset_y
        
        self.canvas.coords(self.rect, self.x, self.y, self.x + 100, self.y + 50)
        self.canvas.coords(self.label, self.x + 50, self.y + 25)

class BlockCodingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Block Coding App")

        self.canvas = tk.Canvas(root, width=600, height=400)
        self.canvas.pack()

        # Add some sample blocks
        self.block1 = Block(self.canvas, 50, 50, "Print")
        self.block2 = Block(self.canvas, 50, 150, "Move")
        self.block3 = Block(self.canvas, 50, 250, "Repeat")

        # Add a button to execute code (just a placeholder for now)
        self.run_button = tk.Button(root, text="Run", command=self.run_code)
        self.run_button.pack()
    
    def run_code(self):
        print("Running code...")
        # Here, you'd add code to run the blocks in a sequence, e.g., executing the actions represented by blocks.
        # You can interpret the block texts and simulate the actions they represent.

if __name__ == "__main__":
    root = tk.Tk()
    app = BlockCodingApp(root)
    root.mainloop()


import tkinter as tk
import random
import math

class AimTrainer:
    def __init__(self, root):
        self.root = root
        self.root.title("Aim Trainer")
        self.root.geometry("800x600")
        self.score = 0
        self.running = False

        self.info = tk.Label(
            root, text="Aim Trainer | Score: 0",
            font=("Arial", 18)
        )
        self.info.pack(pady=10)

        self.canvas = tk.Canvas(
            root, width=760, height=450,
            bg="#10141d", highlightthickness=0
        )
        self.canvas.pack()

        self.button = tk.Button(
            root, text="Start Training",
            command=self.start, font=("Arial", 14)
        )
        self.button.pack(pady=12)

        self.target = None
        self.canvas.bind("<Button-1>", self.shoot)
        self.spawn()

    def spawn(self):
        self.canvas.delete("target")
        x = random.randint(35, 725)
        y = random.randint(35, 415)
        r = 22
        self.target = (x, y, r)

        self.canvas.create_oval(
            x-r, y-r, x+r, y+r,
            outline="#55d6be", width=3, tags="target"
        )
        self.canvas.create_oval(
            x-7, y-7, x+7, y+7,
            fill="#ff5364", tags="target"
        )

    def start(self):
        self.score = 0
        self.running = True
        self.info.config(text="Aim Trainer | Score: 0")
        self.spawn()

    def shoot(self, event):
        if not self.running:
            return

        x, y, r = self.target
        if math.hypot(event.x-x, event.y-y) <= r:
            self.score += 1
            self.info.config(
                text=f"Aim Trainer | Score: {self.score}"
            )
            self.spawn()

root = tk.Tk()
app = AimTrainer(root)
root.mainloop()

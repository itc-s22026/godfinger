import math
import random


class Block:

    def __init__(self, canvas, color):

        self.canvas = canvas
        

        self.id = self.canvas.create_rectangle(50, 50, 150, 75, fill=color)

        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()

        self.init_x = self.canvas_width / 2 - 10
        self.init_y = self.canvas_height / 2 - 250


        self.speed = 0
        
        self.x = 0

        self.y = 0
        
        self.canvas.moveto(self.id, self.canvas_width / 2 - 50, 100)


    def start(self, evt):
        if self.speed != 0:
            return

        self.canvas.moveto(self.id, self.init_x, self.init_y)
        self.speed = 10

        angle = math.radians(random.choice(list(range(20, 65, 5))))
        direction = random.choice([1, -1])
        
        self.x = math.cos(angle) * self.speed * direction
        self.y = math.sin(angle) * self.speed

        #self.canvas.create_text(350, 300, text="GAME START", font=("", 40), fill="GOLD", tag="ai")
        
        

    def draw(self):

        self.canvas.move(self.id, self.x, 0)
        
        pos = self.canvas.coords(self.id)
        if(pos) == 0:
            self.failed()

        
        if pos[0] <= 0:
            self.fix(pos[0] - 0, 0)
        
        if pos[2] >= self.canvas_width:
            self.fix(pos[2] - self.canvas_width, 0)

    def fix(self, diff_x, diff_y):

        self.canvas.move(self.id, -(diff_x * 2), -(diff_y * 2))

        if diff_x != 0:
            self.x = -self.x

        if diff_y != 0:
            self.y = -self.y

    def failed(self):

        self.x = 0
        self.y = 0
        self.speed = 0

    def delete(self):
        self.canvas.delete(self.block.id)
        

        




    









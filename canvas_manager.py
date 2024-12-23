from tkinter import Canvas, NW
from PIL import ImageTk, Image


class CanvasManager:
    def __init__(self, root):
        self.canvas = Canvas(root, bg='black')
        self.canvas.pack(fill='both', expand=True)
        self.tk_img = None
        self.img = None
        self.offset_x = 0
        self.offset_y = 0
        self.is_panning = False
        self.pan_start_x = 0
        self.pan_start_y = 0
        self.is_drawing = False

        # On stocke les IDs de binding pour les événements de panning
        self.start_pan_id = self.canvas.bind("<Button-1>", self.start_pan)
        self.pan_id = self.canvas.bind("<B1-Motion>", self.pan)
        self.end_pan_id = self.canvas.bind("<ButtonRelease-1>", self.end_pan)

    def display_image(self, img, offset_x=0, offset_y=0):
        self.canvas.delete("all")
        self.img = img
        self.tk_img = ImageTk.PhotoImage(img)
        self.canvas.create_image(offset_x, offset_y, anchor=NW, image=self.tk_img)

    def start_pan(self, event):
        if not self.is_drawing:
            self.is_panning = True
            self.pan_start_x, self.pan_start_y = event.x, event.y

    def pan(self, event):
        if self.is_panning and self.img:
            self.offset_x += event.x - self.pan_start_x
            self.offset_y += event.y - self.pan_start_y
            self.pan_start_x, self.pan_start_y = event.x, event.y
            self.display_image(self.img, self.offset_x, self.offset_y)

    def end_pan(self, event):
        self.is_panning = False

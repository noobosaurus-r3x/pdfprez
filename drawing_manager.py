class DrawingManager:
    def __init__(self, canvas, canvas_manager):
        self.canvas = canvas
        self.canvas_manager = canvas_manager
        self.drawing = False
        self.last_draw = None
        self.last_drawn_objects = []
        self.current_drawn_objects = []
        # IDs pour le dessin
        self.draw_motion_id = None
        self.draw_release_id = None

    def toggle_draw(self):
        self.drawing = not self.drawing
        self.canvas_manager.is_drawing = self.drawing
        if self.drawing:
            self.enable_drawing()
            print("Drawing mode enabled")
        else:
            self.disable_drawing()
            print("Drawing mode disabled")

    def enable_drawing(self):
        # On unbind les événements de panning via leurs IDs, pour ne pas tout supprimer
        self.canvas.unbind("<Button-1>", self.canvas_manager.start_pan_id)
        self.canvas.unbind("<B1-Motion>", self.canvas_manager.pan_id)
        self.canvas.unbind("<ButtonRelease-1>", self.canvas_manager.end_pan_id)

        # On bind les événements de dessin et on stocke les IDs
        self.draw_motion_id = self.canvas.bind('<B1-Motion>', self.draw)
        self.draw_release_id = self.canvas.bind('<ButtonRelease-1>', self.reset_last_draw)

    def disable_drawing(self):
        # On unbind seulement les événements de dessin
        if self.draw_motion_id:
            self.canvas.unbind('<B1-Motion>', self.draw_motion_id)
            self.draw_motion_id = None
        if self.draw_release_id:
            self.canvas.unbind('<ButtonRelease-1>', self.draw_release_id)
            self.draw_release_id = None

        # On rebinde panning avec les IDs originaux
        self.canvas_manager.start_pan_id = self.canvas.bind("<Button-1>", self.canvas_manager.start_pan)
        self.canvas_manager.pan_id = self.canvas.bind("<B1-Motion>", self.canvas_manager.pan)
        self.canvas_manager.end_pan_id = self.canvas.bind("<ButtonRelease-1>", self.canvas_manager.end_pan)

    def draw(self, event):
        if self.last_draw is not None:
            x1, y1 = self.last_draw
            x2, y2 = event.x, event.y
            line = self.canvas.create_line(x1, y1, x2, y2, fill='red', width=2)
            self.current_drawn_objects.append(line)
        self.last_draw = (event.x, event.y)

    def reset_last_draw(self, event):
        self.last_draw = None
        if self.current_drawn_objects:
            self.last_drawn_objects.append(self.current_drawn_objects[:])
        self.current_drawn_objects = []

    def delete_last_draw(self):
        if self.last_drawn_objects:
            last_draw = self.last_drawn_objects.pop()
            for obj in last_draw:
                self.canvas.delete(obj)
            print("Last drawing deleted")

    def clear_drawings(self):
        for obj_list in self.last_drawn_objects:
            for obj in obj_list:
                self.canvas.delete(obj)
        self.last_drawn_objects = []
        self.current_drawn_objects = []
        print("All drawings cleared")

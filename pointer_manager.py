class PointerManager:
    def __init__(self, canvas):
        self.canvas = canvas
        self.pointer_mode = False
        self.pointer_indicator = None

    def toggle_pointer(self):
        """Toggle pointer mode."""
        self.pointer_mode = not self.pointer_mode
        if self.pointer_mode:
            self.canvas.bind('<Motion>', self.show_pointer)
            self.canvas.master.config(cursor='none')
            print("Pointer mode enabled")
        else:
            self.canvas.unbind('<Motion>')
            if self.pointer_indicator:
                self.canvas.delete(self.pointer_indicator)
                self.pointer_indicator = None
            self.canvas.master.config(cursor='arrow')
            print("Pointer mode disabled")

    def show_pointer(self, event):
        """Display a pointer on the canvas."""
        if self.pointer_indicator:
            self.canvas.delete(self.pointer_indicator)
        self.pointer_indicator = self.canvas.create_oval(
            event.x - 5, event.y - 5, event.x + 5, event.y + 5,
            outline='red', fill='red'
        )

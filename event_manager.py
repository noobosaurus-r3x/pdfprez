class EventManager:
    def __init__(self, root, viewer):
        self.root = root
        self.viewer = viewer
        self.bind_events()

    def bind_events(self):
        self.root.bind('<Right>', self.viewer.next_page)
        self.root.bind('<Left>', self.viewer.previous_page)
        self.root.bind('<Escape>', self.viewer.quit_program)
        self.root.bind('<Key-f>', self.viewer.toggle_fullscreen)
        self.root.bind('<Key-d>', self.viewer.toggle_draw)
        self.root.bind('=', lambda event: self.viewer.zoom('in'))
        self.root.bind('+', lambda event: self.viewer.zoom('in'))
        self.root.bind('-', lambda event: self.viewer.zoom('out'))
        self.root.bind('<Key-h>', self.viewer.show_help_screen)

        self.viewer.canvas_manager.canvas.bind("<Button-1>", self.viewer.canvas_manager.start_pan)
        self.viewer.canvas_manager.canvas.bind("<B1-Motion>", self.viewer.canvas_manager.pan)
        self.viewer.canvas_manager.canvas.bind("<ButtonRelease-1>", self.viewer.canvas_manager.end_pan)

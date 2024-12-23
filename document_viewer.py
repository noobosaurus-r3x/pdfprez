import tkinter as tk
from pdf_renderer import PDFRenderer
from canvas_manager import CanvasManager
from drawing_manager import DrawingManager
from pointer_manager import PointerManager
from help_screen import HelpScreen
from splash_screen import SplashScreen
from tkinter import messagebox


class DocumentViewer:
    def __init__(self, root, filepath=None):
        self.root = root
        self.root.title("Document Presenter")
        self.root.geometry("1024x768")

        # Initialisation des modules
        self.renderer = PDFRenderer()
        self.canvas_manager = CanvasManager(self.root)
        self.drawing_manager = DrawingManager(self.canvas_manager.canvas, self.canvas_manager)
        self.pointer_manager = PointerManager(self.canvas_manager.canvas)

        self.current_page = 0

        if filepath:
            self.load_pdf(filepath)
            self.display_page()
            self.bind_events()
        else:
            # Afficher la splash screen
            self.splash_screen = SplashScreen(self.root, self.on_file_selected)

    def on_file_selected(self, filepath):
        """Callback appelé lorsque l'utilisateur sélectionne un fichier PDF depuis la splash screen."""
        self.load_pdf(filepath)
        self.display_page()
        self.bind_events()

    def load_pdf(self, filepath):
        """Charge un fichier PDF et affiche le canevas."""
        try:
            self.renderer.load(filepath)
            img = self.renderer.render_page(self.current_page)
            self.canvas_manager.display_image(img, self.canvas_manager.offset_x, self.canvas_manager.offset_y)
            self.show_canvas()
        except Exception as e:
            print(f"Erreur lors du chargement du PDF : {e}")
            messagebox.showerror("Erreur", "Impossible de charger le fichier PDF.")

    def bind_events(self):
        """Lie les événements clavier et souris."""
        self.root.bind('<Right>', self.next_page)
        self.root.bind('<Left>', self.previous_page)
        self.root.bind('<Escape>', self.quit_program)
        self.root.bind('<Key-f>', self.toggle_fullscreen)
        self.root.bind('<Key-d>', lambda event: self.toggle_draw_mode())
        self.root.bind('<Key-p>', lambda event: self.pointer_manager.toggle_pointer())
        self.root.bind('=', lambda event: self.zoom('in'))
        self.root.bind('+', lambda event: self.zoom('in'))
        self.root.bind('-', lambda event: self.zoom('out'))
        self.root.bind('<Key-h>', lambda event: HelpScreen.show(self.root))
        self.root.bind('<Delete>', lambda event: self.drawing_manager.clear_drawings())
        self.root.bind('<BackSpace>', lambda event: self.drawing_manager.delete_last_draw())

    def toggle_draw_mode(self):
        """Bascule entre le mode dessin et le mode panning."""
        self.drawing_manager.toggle_draw()

    def display_page(self):
        """Affiche la page courante du PDF."""
        if self.renderer:
            img = self.renderer.render_page(self.current_page)
            if img:
                self.canvas_manager.display_image(img, self.canvas_manager.offset_x, self.canvas_manager.offset_y)

    def zoom(self, direction):
        """Gère le zoom avant/arrière."""
        zoom_step = 0.05
        if direction == 'in':
            self.renderer.set_scale(self.renderer.scale + zoom_step)
        elif direction == 'out' and self.renderer.scale > 0.2:
            self.renderer.set_scale(self.renderer.scale - zoom_step)
        self.display_page()

    def next_page(self, event=None):
        """Passe à la page suivante."""
        if self.renderer and self.current_page < len(self.renderer.doc) - 1:
            self.current_page += 1
            self.display_page()

    def previous_page(self, event=None):
        """Revient à la page précédente."""
        if self.renderer and self.current_page > 0:
            self.current_page -= 1
            self.display_page()

    def toggle_fullscreen(self, event=None):
        """Bascule le mode plein écran."""
        self.root.attributes('-fullscreen', not self.root.attributes('-fullscreen'))

    def quit_program(self, event=None):
        """Quitte l'application."""
        if self.renderer:
            self.renderer.close()
        self.root.destroy()

    def show_canvas(self):
        """Affiche le canevas après le chargement du PDF."""
        self.canvas_manager.canvas.pack(fill=tk.BOTH, expand=True)

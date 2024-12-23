import fitz  # PyMuPDF
from PIL import Image


class PDFRenderer:
    def __init__(self, filepath=None):
        self.filepath = filepath
        self.doc = None
        self.scale = 1.0  # Échelle par défaut

        if filepath:
            self.load(filepath)

    def load(self, filepath):
        """Charge un fichier PDF."""
        self.filepath = filepath
        self.doc = fitz.open(filepath)

    def render_page(self, page_num=0):
        """Rend une page PDF sous forme d'image."""
        if self.doc is None:
            raise ValueError("Aucun document PDF n'est chargé.")
        
        page = self.doc.load_page(page_num)
        pix = page.get_pixmap(dpi=int(150 * self.scale))
        img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
        return img

    def set_scale(self, scale):
        """Définit l'échelle pour le rendu."""
        self.scale = scale

    def close(self):
        """Ferme le document PDF."""
        if self.doc:
            self.doc.close()

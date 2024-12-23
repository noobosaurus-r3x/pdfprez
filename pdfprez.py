import tkinter as tk
from document_viewer import DocumentViewer
import sys
import os


def main():
    if len(sys.argv) > 1:
        pdf_filepath = sys.argv[1]
        if not os.path.isfile(pdf_filepath) or not pdf_filepath.lower().endswith('.pdf'):
            print("Error: Invalid PDF file.")
            sys.exit(1)
    else:
        pdf_filepath = None

    root = tk.Tk()
    DocumentViewer(root, filepath=pdf_filepath)
    root.mainloop()


if __name__ == "__main__":
    main()

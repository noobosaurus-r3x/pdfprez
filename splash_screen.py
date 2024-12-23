import tkinter as tk
from tkinter import filedialog, messagebox


class SplashScreen:
    def __init__(self, root, on_file_selected):
        self.root = root
        self.on_file_selected = on_file_selected  # Callback lorsque le fichier est sélectionné

        # Masquer le canevas existant (s'il existe déjà)
        for widget in root.winfo_children():
            widget.pack_forget()

        # Créer un cadre pour la splash screen
        self.frame = tk.Frame(root, bg="#232136")
        self.frame.pack(fill=tk.BOTH, expand=True)

        # Titre
        title = tk.Label(
            self.frame,
            text="Bienvenue dans Document Presenter!",
            font=("Helvetica", 18, "bold"),
            bg="#2a273f",
            fg="#c4a7e7"
        )
        title.pack(pady=20)

        # Instruction
        instruction = tk.Label(
            self.frame,
            text="Veuillez sélectionner un fichier PDF pour commencer ou quitter.",
            font=("Helvetica", 14),
            bg="#232136",
            fg="#9ccfd8"
        )
        instruction.pack(pady=10)

        # Bouton pour ouvrir un fichier PDF
        open_button = tk.Button(
            self.frame,
            text="Ouvrir un fichier PDF",
            command=self.open_file,
            font=("Helvetica", 14),
            bg="#4CAF50",
            fg="#ffffff",
            padx=10,
            pady=5
        )
        open_button.pack(pady=10)

        # Bouton pour quitter
        exit_button = tk.Button(
            self.frame,
            text="Quitter",
            command=self.quit_program,
            font=("Helvetica", 14),
            bg="#e74c3c",
            fg="#ffffff",
            padx=10,
            pady=5
        )
        exit_button.pack(pady=10)

    def open_file(self):
        """Ouvre une boîte de dialogue pour sélectionner un fichier PDF."""
        filepath = filedialog.askopenfilename(
            title="Ouvrir un fichier PDF",
            filetypes=[('Fichiers PDF', '*.pdf')]
        )
        if filepath and self.is_valid_pdf(filepath):
            self.frame.destroy()  # Supprimer la splash screen
            self.on_file_selected(filepath)  # Appeler le callback avec le chemin du fichier
        else:
            messagebox.showerror("Erreur", "Fichier PDF invalide sélectionné.")

    @staticmethod
    def is_valid_pdf(filepath):
        """Valide si le fichier sélectionné est un PDF."""
        try:
            with open(filepath, 'rb') as f:
                header = f.read(4)
                return header == b'%PDF'
        except Exception as e:
            print(f"Erreur lors de la validation du PDF : {e}")
            return False

    def quit_program(self):
        """Quitte l'application."""
        self.root.destroy()

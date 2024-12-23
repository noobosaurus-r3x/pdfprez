import tkinter as tk


class HelpScreen:
    @staticmethod
    def show(root):
        """Display a help screen."""
        help_window = tk.Toplevel(root)
        help_window.title("Help - Key Commands")
        help_window.geometry("600x400")
        help_window.config(bg="#232136")

        help_text = """
Right Arrow: Next page
Left Arrow: Previous page
f: Toggle fullscreen
d: Toggle drawing mode
p: Toggle pointer mode
Delete: Clear all drawings
Backspace: Undo last drawing
+ or =: Zoom in
-: Zoom out
h: Show this help screen
Escape: Quit program
Mouse Drag: Pan across the page
        """

        header = tk.Label(help_window, text="Help - Key Commands", font=("Consolas", 18, "bold"), bg="#2a273f", fg="#f6c177")
        header.pack(fill=tk.X, pady=10)

        content = tk.Label(help_window, text=help_text, font=("Consolas", 14), bg="#232136", fg="#9ccfd8", justify=tk.LEFT, padx=10)
        content.pack(pady=10)

        close_button = tk.Button(help_window, text="Close", command=help_window.destroy, bg="#e74c3c", fg="white", font=("Consolas", 14))
        close_button.pack(pady=10)


# PDFPREZ

PDFPREZ is a Python application designed for presenting PDF documents interactively. It supports features such as drawing annotations, pointer mode, zooming, panning, and seamless navigation between pages, making it ideal for presentations.

## Features

- **Load and Display PDFs**: Open and present any PDF file in fullscreen mode.
- **Navigation**: Use keyboard arrows to move between pages.
- **Drawing Mode**: Annotate PDF pages interactively with freehand drawing.
- **Pointer Mode**: Highlight specific areas of the page with a virtual pointer.
- **Zooming**: Zoom in and out for better clarity.
- **Panning**: Move around the page when zoomed in using mouse drag.
- **Help Screen**: Quickly view all key commands within the application.
- **Error Handling**: User-friendly error messages with logging for troubleshooting.

## Installation

Clone the repository:

```bash
git clone https://github.com/noobosaurus-r3x/pdfprez
```

### Install Dependencies

Install the required packages:

```bash
pip install -r requirements.txt
```

### Usage

Run the application:

```bash
python3 pdfprez.py [path_to_pdf]
```

- If `[path_to_pdf]` is provided, the PDF will load automatically.
- Without a PDF file, a splash screen will allow you to select one.

### Key Commands

- **`Right Arrow`**: Next page
- **`Left Arrow`**: Previous page
- **`f`**: Toggle fullscreen
- **`d`**: Toggle drawing mode
- **`p`**: Toggle pointer mode
- **`=`** or **`+`**: Zoom in
- **`-`**: Zoom out
- **`Mouse Drag`**: Pan across the page
- **`Delete`**: Clear all drawings
- **`Backspace`**: Undo last drawing
- **`h`**: Show help screen
- **`Escape`**: Quit program

### Zoom and Panning

- **Zooming**: Use `=` or `+` to zoom in and `-` to zoom out.
- **Panning**: Click and drag the mouse to move around the zoomed-in page.

### Logging

Errors and exceptions are logged to `pdfprez.log` in the application directory.

## Development

Look, I'm not a professional developer — just someone messing around with Python and PDFs. PDFPREZ isn't a war machine, but it works surprisingly well and gets the job done. If it helps you too, great! Feel free to fork the repo and tweak it as you like.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

Enjoy seamless PDF presentations with **pdfprez** — simple, functional, and just a little bit scrappy!

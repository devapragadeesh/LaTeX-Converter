# LaTeXConverter (LaTeX-OCR)
![MIT License](https://img.shields.io/badge/License-MIT-green.svg?style=flat-square)
![Repo Size](https://img.shields.io/github/repo-size/devapragadeesh/LaTeX-Converter?style=flat-square)
![Last Commit](https://img.shields.io/github/last-commit/devapragadeesh/LaTeX-Converter?style=flat-square)
![Python](https://img.shields.io/badge/python-3.8+-blue.svg?style=flat-square)

<img width="500" height="453" alt="LatexCon" src="https://github.com/user-attachments/assets/8b68886c-12e6-4a76-8d9f-3f05b8a7a193" />


A custom extension that:
- Preprocesses the image before extraction for a higher rate of accuracy.
- Converts math images to LaTeX.
- Renders LaTeX into styled PNG images and PDF format as well.
- Adds custom scripts for rendering, automation,and formatting.


## Tool Objective:
Convert math question images into usable, editable LaTeX code and render the result into an image for reuse in:
- Educational content
- Scientific papers
- Digital documentation
- Exam generation

---

## Input

- Any math image file ('.png', '.jpg', etc.)
- Provided as a command-line argument or in code

---

## Workflow Overview

The following diagram outlines the full process from raw math image to rendered LaTeX output.
<img width="400" height="800" alt="Untitled diagram _ Mermaid Chart-2025-08-05-152628" src="https://github.com/user-attachments/assets/1011ced9-5dfd-431a-81cc-b743c8c6b207" />

---

## Example Run

This example demonstrates how a math image is converted into LaTeX and then rendered back as a polished output image.

---

### Input Image

This is the raw image of a math question passed into the tool.

Example:

<img width="250" height="250" alt="mathdoubt" src="https://github.com/user-attachments/assets/8a36b1f8-78b0-4f60-aeec-58d1951edde5" />


---

### Extracted LaTeX

The LaTeX code extracted using the 'pix2tex' model is printed below:

```latex
\int_{0}^{\pi} \sin(x)\,dx
```
---

## Folder Structure

All custom code ('extract.py', 'render_latex.py') lives inside the 'LaTeX-OCR/' folder for import compatibility.

```bash
LaTeXConverter/
├── LaTeX-OCR/
│   ├── extract.py
│   ├── render_latex.py
│   └── ...
├── assets/
│   ├── mathdoubt.png
│   ├── rendered_latex.png
├── README.md
├── LICENSE
├── requirements.txt
```
---

## Usage

```bash
python LaTeX-OCR/extract.py --input assets/mathdoubt.png
```
## Acknowledgement:
Code Modified From: [Lukas Blecher](https://github.com/lukas-blecher/LaTeX-OCR)

## Contact

**Devapragadeesh B**   
🔗 [GitHub](https://github.com/devapragadeesh)  
=======

import os
import subprocess
from pdf2image import convert_from_path

def write_latex_file(latex_code, tex_path):
    with open(tex_path, "w", encoding="utf-8") as f:
        f.write(r"""\documentclass[preview]{standalone}
\usepackage{amsmath}
\usepackage{amsfonts}
\usepackage{amssymb}
\begin{document}
""" + "\n" + latex_code + "\n\\end{document}")

def compile_latex_to_pdf(tex_path, output_dir):
    subprocess.run([
        "pdflatex",
        "-interaction=nonstopmode",
        "-output-directory", output_dir,
        tex_path
    ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

def convert_pdf_to_image(pdf_path, output_image_path):
    images = convert_from_path(pdf_path, dpi=300)
    images[0].save(output_image_path, "PNG")

def render_latex_to_image(latex_code, filename="output"):
    tex_path = f"{filename}.tex" #eg: output.tex
    pdf_path = f"{filename}.pdf" #eg: output.pdf
    image_path = f"{filename}.png" #eg: output.png

    write_latex_file(latex_code, tex_path) #writing .tex file 
    compile_latex_to_pdf(tex_path, ".") #compiling .tex to .pdf
    convert_pdf_to_image(pdf_path, image_path) #converting .pdf to .png

    print(f"Image saved to {image_path}")

if __name__ == "__main__":
    sample_latex = r"\[\frac{11+x}{x^{3}}\]"
    render_latex_to_image(sample_latex, filename="latex_render")

import matplotlib.pyplot as plt
import os

def render_latex_to_image(latex_code, output_path="rendered_latex.png", dpi=300):
    # Start a new figure
    fig, ax = plt.subplots(figsize=(6, 2))
    fig.patch.set_visible(False)
    ax.axis("off")

    # Format the LaTeX code
    formatted_code = f"${latex_code}$"  # add math mode delimiters

    # Render the LaTeX text
    ax.text(0.5, 0.5, formatted_code, fontsize=20, ha='center', va='center')

    # Save to file
    plt.savefig(output_path, bbox_inches="tight", pad_inches=0.2, dpi=dpi, transparent=True)
    plt.close()
    print(f"LaTeX rendered and saved to: {output_path}")

# Example usage
if __name__ == "__main__":
    sample_latex = r"{\frac{9}{\sqrt{x-1}}}"
    render_latex_to_image(sample_latex)

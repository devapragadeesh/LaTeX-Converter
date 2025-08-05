from pix2tex.cli import LatexOCR
from PIL import Image, ImageOps, ImageEnhance

def preprocess_image(image_path):
    img = Image.open(image_path).convert("L") #Grayscale
    img = ImageOps.invert(img) #Invert if background is white for better identification
    img = ImageOps.autocontrast(img)     #Autocontrast
    enhancer = ImageEnhance.Sharpness(img)
    img = enhancer.enhance(2.0)          #Sharpen
    return img

# Initialize model
ocr_model = LatexOCR()

# Preprocess image
img_path = "mathdoubt.png"
img = preprocess_image(img_path)

# Predict LaTeX
latex_code = ocr_model(img)

print("Predicted LaTeX:")
print(latex_code)
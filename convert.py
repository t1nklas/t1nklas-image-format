import struct
import tkinter as tk
from tkinter import filedialog
from PIL import Image

def save_t1nklas(filename, width, height, pixels):
    with open(filename, "wb") as f:
        f.write(b"T1NK")
        f.write(struct.pack("<HHB", width, height, 8))
        
        for r, g, b, a in pixels:
            f.write(struct.pack("BBBB", r, g, b, a))

def convert_image_to_t1nklas():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.bmp;*.gif")])
    
    if not file_path:
        print("No file selected.")
        return
    
    image = Image.open(file_path).convert("RGBA")
    width, height = image.size
    pixels = list(image.getdata())
    
    save_path = filedialog.asksaveasfilename(defaultextension=".t1nklas", filetypes=[("T1NKLAS Files", "*.t1nklas")])
    if save_path:
        save_t1nklas(save_path, width, height, pixels)
        print(f"Image saved as {save_path}")
    else:
        print("Save operation cancelled.")

if __name__ == "__main__":
    convert_image_to_t1nklas()

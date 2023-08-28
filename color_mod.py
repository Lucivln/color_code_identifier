import cv2
import numpy as np
import tkinter as tk
from tkinter import filedialog, messagebox
try:
    import webcolors
except ImportError:
    pass

class ColorExtractorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Color Extractor")
        
        self.label = tk.Label(root, text="Select an image:")
        self.label.pack(pady=10)
        
        self.button = tk.Button(root, text="Browse", command=self.browse_image)
        self.button.pack()
        
        self.result_text = tk.Text(root, wrap=tk.WORD)
        self.result_text.pack(pady=10)
        
    def browse_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png")])
        if file_path:
            color_info = self.extract_colors(file_path, num_colors_to_extract=5)
            self.display_color_info(color_info)
        else:
            messagebox.showinfo("Info", "No image selected.")
        
    def extract_colors(self, image_path, num_colors_to_extract):
        image = cv2.imread(image_path)
        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        pixels = image_rgb.reshape(-1, 3)
        
        criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 200, 0.1)
        _, labels, centers = cv2.kmeans(pixels.astype(np.float32), num_colors_to_extract, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)
        dominant_colors = centers.astype(np.uint8)
        color_codes = ['#%02x%02x%02x' % (r, g, b) for r, g, b in dominant_colors]
        
        color_info = []
        for r, g, b in dominant_colors:
            try:
                color_name = webcolors.rgb_to_name((r, g, b))
            except ValueError:
                color_name = "Unknown"
            color_info.append((color_name, '#%02x%02x%02x' % (r, g, b)))
        
        return color_info
    
    def display_color_info(self, color_info):
        self.result_text.delete(1.0, tk.END)
        for idx, (color_name, color_code) in enumerate(color_info, start=1):
            result = f"Color {idx}: {color_name} ({color_code})\n"
            self.result_text.insert(tk.END, result)

def main():
    root = tk.Tk()
    app = ColorExtractorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()

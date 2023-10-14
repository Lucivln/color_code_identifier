import cv2
import numpy as np
import tkinter as tk
from tkinter import filedialog, messagebox
import mysql.connector
from tkinter import ttk

try:
    import webcolors
except ImportError:
    pass

# Connect to the MySQL server
conn = mysql.connector.connect(
    host="localhost",
    user="yourusername",#add your mysql username
    password="yourpassword",#add your password
    database="colordb"
)
c = conn.cursor()

# Create a table for storing image paths and color information
c.execute('''CREATE TABLE IF NOT EXISTS ColorData
             (id INT AUTO_INCREMENT PRIMARY KEY, image_path TEXT, color_name TEXT, color_code TEXT)''')
conn.commit()

class ColorExtractorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Color Extractor")

        # Set the custom icon for the taskbar
        self.root.iconbitmap('your custom icon') #add the path to your custom image icon

        self.label = tk.Label(root, text="Select an image:")
        self.label.pack(pady=10)

        self.button = tk.Button(root, text="Browse", command=self.browse_image)
        self.button.pack()

        self.result_tree = ttk.Treeview(root)
        self.result_tree["columns"] = ("ID", "Image Path", "Color Name", "Color Code")
        self.result_tree.heading("#0", text="", anchor="w")
        self.result_tree.heading("ID", text="ID")
        self.result_tree.heading("Image Path", text="Image Path")
        self.result_tree.heading("Color Name", text="Color Name")
        self.result_tree.heading("Color Code", text="Color Code")
        self.result_tree.pack(pady=10)

    def browse_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png")])
        if file_path:
            color_info = self.extract_colors(file_path, num_colors_to_extract=5)
            self.display_color_info(color_info)
            self.store_color_data(file_path, color_info)
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
        self.result_tree.delete(*self.result_tree.get_children())
        for idx, (color_name, color_code) in enumerate(color_info, start=1):
            self.result_tree.insert("", "end", values=(idx, color_info[0][0], color_name, color_code))
        
        # Set the width of the columns
        self.result_tree.column("#0", width=500, minwidth=500, anchor="center")
        self.result_tree.column("Image Path", width=300, minwidth=200)
        self.result_tree.column("Color Name", width=100, minwidth=80)
        self.result_tree.column("Color Code", width=100, minwidth=80)

    def store_color_data(self, image_path, color_info):
        for color_name, color_code in color_info:
            c.execute("INSERT INTO ColorData (image_path, color_name, color_code) VALUES (%s, %s, %s)",
                      (image_path, color_name, color_code))
        conn.commit()

    def view_data(self):
        c.execute("SELECT * FROM ColorData")
        data = c.fetchall()
        self.result_tree.delete(*self.result_tree.get_children())
        for row in data:
            self.result_tree.insert("", "end", values=row)

def main():
    root = tk.Tk()
    app = ColorExtractorApp(root)
    app.view_data()  # Call the view_data method to display the data

    root.iconbitmap('your custom icon') #add the path to your custom image icon

    root.mainloop()

if __name__ == "__main__":
    main()

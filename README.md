 ## Color Extractor App

This is a simple Python application that extracts the dominant colors from an image. The app uses the k-means clustering algorithm to identify the most common colors in an image and then displays them in a list. Additionally, it stores the color information in a MySQL database.

### Prerequisites

To run this app, you will need the following:

* Python 3.6 or later
* The `tkinter` library
* The `opencv-python` library
* The mysql-connector-python library (for MySQL database interaction)
* The `webcolors` library (optional)

### Installation

To install the app, clone the repository and install the required libraries:

```
git clone https://github.com/Lucivln/color_code_identifier.git
cd color_code_identifier
pip install -r requirements.txt
```

### Usage

* To use the app, simply run the `color_mod.py` file:

```
python color_mod.py
```

* The app will open a graphical user interface (GUI) window.
* Click the "Browse" button to select an image.
* The app will extract the dominant colors from the image and display them in a list within the GUI.
* The color information is also stored in a MySQL database named "colordb" for future reference.

### Code Explanation

The code for the app is organized as follows:

* It establishes a connection to a MySQL database where color data will be stored.
* It creates a table named 'ColorData' in the database to store image paths, color names, and color codes.
* The 'ColorExtractorApp' class contains methods for extracting, displaying, and storing color information.
* The 'browse_image' method allows users to select an image, and then it calls the 'extract_colors' and 'store_color_data' methods.
* The 'extract_colors' method uses the k-means clustering algorithm to find dominant colors in the selected image.
* The 'display_color_info' method displays the dominant colors in the GUI.
* The 'store_color_data' method stores color information in the MySQL database.
* The 'view_data' method retrieves and displays stored color data from the database.
* The main function initializes the tkinter window, creates an instance of the ColorExtractorApp class, and displays any existing color data.

### Customization

* You can customize the GUI icon by replacing 'your custom icon' with the path to your own image icon in the code.
* Make sure to update the database connection details by providing your MySQL username and password in the conn variable.
* If you want to use the webcolors library for color naming, make sure it is installed.
* The code currently extracts the top 5 dominant colors; you can change the value in the num_colors_to_extract parameter when calling extract_colors.

### Conclusion

This simple but useful app can be used to extract and store dominant colors from images. It offers an easy-to-use interface and is suitable for users with various levels of technical expertise. You can further customize the app, including adding your custom icon for a personalized touch.
This app provides a simple but useful way to extract and store dominant colors from images and can be easily used by individuals with various levels of technical expertise.

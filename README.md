 ## Color Extractor App

This is a simple Python application that extracts the dominant colors from an image. The app uses the k-means clustering algorithm to identify the most common colors in an image and then displays them in a list.

### Prerequisites

To run this app, you will need the following:

* Python 3.6 or later
* The `tkinter` library
* The `opencv-python` library
* The `webcolors` library (optional)

### Installation

To install the app, clone the repository and install the required libraries:

```
git clone https://github.com/Lucivln/color_code_identifier.git
cd color_code_identifier
pip install -r requirements.txt
```

### Usage

To use the app, simply run the `color_mod.py` file:

```
python color_mod.py
```

The app will then prompt you to select an image. Once you have selected an image, the app will extract the dominant colors and display them in a list.

### Code Explanation

The code for the app is relatively simple. The main function creates a `tkinter` window and then creates a `ColorExtractorApp` object. The `ColorExtractorApp` class contains the methods that are responsible for extracting the colors from an image and displaying them in a list.

The `extract_colors()` method uses the k-means clustering algorithm to identify the most common colors in an image. The method first converts the image to the RGB color space and then reshapes the image into a one-dimensional array. The method then uses the `cv2.kmeans()` function to cluster the pixels in the image into a specified number of clusters. The method then returns the cluster centers, which represent the dominant colors in the image.

The `display_color_info()` method displays the dominant colors in a list. The method first creates a `tkinter` `Text` widget and then inserts the color names and color codes into the widget.

### Conclusion

This is a simple but useful app that can be used to extract the dominant colors from an image. The app is easy to use and can be used by anyone, regardless of their technical expertise.

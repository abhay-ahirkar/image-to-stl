# Image to STL Converter

This is a web application built with Django that allows users to convert images to STL files.

## Requirements

To run this application, you need to have Python 3 and the following packages installed:

-   Django
-   Pillow
-   NumPy
-   PySTL

You can install them using pip:

Copy code

`pip install Django Pillow numpy stl` 

## Installation

To install this application, follow these steps:

1.  Clone the repository:

bashCopy code

`git clone https://github.com/yourusername/imagetostl.git` 

2.  Change into the project directory:

bashCopy code

`cd imagetostl` 

3.  Create a virtual environment:

bashCopy code

`python -m venv env` 

4.  Activate the virtual environment:

bashCopy code

`source env/bin/activate` 

On Windows, use the following command instead:

bashCopy code

`env\Scripts\activate` 

5.  Install the dependencies:

Copy code

`pip install -r requirements.txt` 

6.  Run the server:

Copy code

`python manage.py runserver` 

The server should now be running at [http://localhost:8000](http://localhost:8000/).

## Usage

To use the application, follow these steps:

1.  Open your web browser and go to [http://localhost:8000](http://localhost:8000/).
    
2.  Click on the "Convert Image to STL" button.
    
3.  Select an image file to upload.
    
4.  Click on the "Convert to STL" button.
    
5.  Wait for the conversion to complete. The page will display a link to download the STL file.
    

## License

This application is released under the MIT License. See LICENSE for details.

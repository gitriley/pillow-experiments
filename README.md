# pillow-experiments
### What it it?
combine.py is a small program that combines two images to create a new composite image. See examples below

### How to use it:
First, make sure you have Pillow (python imaging library) installed.
Run combine.py from the command line with the following command line arguments:

```
argument 1 = the first image
argument 2 = the second image
argument 3 = pixel width of the image slices (a value between 3 - 20 is recommended)
argument 4 = 'vertical' or 'horizontal' - should the images be slices vertically or horizontally?
argument 5 (optional) = 'save'. Include 'save' to write the file to disk. Otherwise, the program will just open up a preview of the output image, but will not save it to disk. It's useful to leave this off if you're just experimenting.
```
For example:
```
$ combine.py img1.jpg img2.jpg 8 vertical save 
```

### What's the purpose of the program?:
This program is just for fun. I was learning python for work and wanted a small side project to get comfortable with the language. I'd always wondered about combining image like this in Photoshop, but it would take hours of meticulous work in Photoshop to create a single composite image. It's much quicker with code.

The majority of images will look like garbage when combined, but if you carefully select photos, you can create some decent images.

### Actual Examples:

combine two photos:
![Alt text](sunset1.jpg?raw=true "Sunset")
![Alt text](moon.jpg?raw=true "Moon")
result:
![Alt text](moonsunjet.jpg?raw=true "Combined")
**(top two photos by [Charlotte Curd](https://www.instagram.com/charlottecurd/))**

combine Mount Fuji and the same photo flipped 180 degrees:
![Alt text](fuji.jpg?raw=true "Mount Fuji")
result:
![Alt text](fujiflip.jpg?raw=true "Mount Fuji")

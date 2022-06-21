
# ASCII Art Project

In this project we have used ASCII characters(like @,$,u,&,*...etc.) available on our keyboard to create images just from these characters. 
As an additional task, **videos as well as live webacam feed** have also been turned into coloured ASCII video. An extra feature that has been added is, we can also change the *style of ASCII characters, background, frame size* in our running video/feed. 

So let's look at this Another Super Cool Interesting Idea(ASCII) for image and video conversion.

![](https://i.imgur.com/op8Ug2K.jpeg)


## How To Run
### Installation
This project was built in python3 programming language and the libraries required were:

* OpenCV
* Numpy (required in video to ASCII part)
* Pillow

**To run** :

1. Open the terminal and locate folder to copy to
2. `git clone https://github.com/sapiann/ASCII_Project_Images_and_Videos.git`
3. Install the libraries
```bash
   $ pip install opencv-python
   $ pip install numpy
   $ pip install pillow 
   ```
 
Once the libraries have been installed we can import them using:
```bash
import cv2
import numpy as np
import math
from PIL import ImageDraw,ImageFont,Image, ImageEnhance
```
### For ASCII conversion of images
* Choose `ascii_image`
* By default an input image that we have selected is open, open your desired image using `img = Image.open()`.
* Select your preferred `bg_colour` and `sequence`.
* Run `python ascii_image.py` and you will get the converted ASCII image.
* For grey scale conversion use `img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)` and follow the comments written in code.

### For ASCII conversion of webcam feed
* Choose `ascii_webcam`.
* The webcam loads by default from `ascii_webcam` by writing in terminal `python ascii_webcam.py`.
* Make sure to allow the program access to your webcam to run.
* You can change the *background, ASCII style, size of frame* using the mentioned keys in program.

### For ASCII conversion of video
* Choose `ascii_video`.
* You can change the video file name if you wish. By default when you run `python ascii_video.py` the ASCII video frame pops up.
* Just like webcam mode, you can change the *background, ASCII style, size of frame* using the mentioned keys in program.



    
## Working Of Project

### Images to ASCII conversion

* After choosing the input image, we get it's dimension :height and width and also select a font type and size to get it's size.
* Then we resize the image based on the character's dimensions and using a scale factor.
* Then we load pixel data to access the pixels of image directly instead of rows, columns.
* We then use features from `Pillow` such as `Image.new()`, `ImageDraw.Draw()` to create an output image of proper size for characters.
* We run a loop to get pixel data along height `i` and width `j` and then get a character using weighted pixel value out of a list of character.
* We specify the font, fill the character using colour value of that pixel.
* For backgrounf you can choose either black or white bg. 
* Characters at end of list are brighter for black bg so the program reverses them for better display.
* Once the loop is over, we enhance the brightness of output image and crop it to get better image.
* Then the final output image pops up and is saved.

### WebCam and Video to ASCII conversion
* For this part we have defined a `Video_to_ASCII` class in our program.
* `main` function is called first that instantiate the class object and begins the feed.
* `style, bg, scale_factor` are the attributes of objects which we can access while the prgram is running to change some features of program.
* Then certain functions are defined under this class for conversion, major part is similar to image conversion only.
* Instead of a single image, we get images in form of frames. We read the video capture, send the frames for conversion and using `np.array()` get frames of output images to be displayed.
* We use `cv2.imshow()` function for showing our output. 
* The procedure for video conversion is also the same except that when using `cv2.VideoCapture(0)` we use `cv2.VideoCapture(file)` where file is name of the video file.


## Learnings and Takeaways

So this ASCII Art Generator is one of my first projects I built using Python. It has been very helpul to gain an understanding
of the language as well as taught me a lot about image processing on RGB and Greyscale images using the mentioned libraries.

It has been really cool to look at a picture then work on it's individual pixels, then transform those pixels into characters and those characters into an awesome ASCII image.
The weekly discussions proved really helpful as I was just a beginner to this stuff. Had to read up a lot of stuff to implement those aditional tasks of converting
video and webcam feed into outputs ASCII videos. So major takeaways would be some python knowledge, some image processing knowledge and some fun :)

So...ig thanks ACM for the opportunity!


## References
All the mentioned resources have proved helpful in building this project.

 - [ACM Weekly discussion files](https://drive.google.com/drive/u/1/folders/1HAtoMM4L06yqbZWDG3nEtepRLPOO-i83)
 - [ASCII Transformer](https://github.com/kailau02/ascii-transformer#webcam-mode)
 - [How digital images are stored in a computer.](https://alekya3.medium.com/how-images-are-stored-in-a-computer-f364d11b4e93)
 - [ASCII video YouTube](https://www.youtube.com/watch?v=55iwMYv8tGI&t=829s)
 - [Wikipedia On ASCII](https://en.wikipedia.org/wiki/ASCII_art)


## Some images we converted

![App Screenshot](https://via.placeholder.com/468x300?text=App+Screenshot+Here)


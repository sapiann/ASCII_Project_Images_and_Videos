
from unittest import main
from PIL import ImageDraw,ImageFont,Image
import cv2
import numpy as np
import math

#shading styles for ASCII characters arranged according to increasing brightness on oppsite bg
Shading_style = {
        "standard": "@%#*+=-:. ",
        "complex": "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ",
        "test": "#Ww. "
    }

#we define a class for conversion, in this way we can access the attributes of object while our program is running and change certain features
#like background colour, ascii style
class Video_to_ASCII:
    def __init__(self, style="standard", bg=False, scale_factor =0.08):
       self.style = Shading_style[style]
       self.bg = bg
       self.scale_factor = scale_factor
       #bg here is a boolean variable (false for white bg, True for black)
       #shading style adjusts according to bg
       if bg:
        self.style = self.style[::-1]
 
    def imagify(self, img = None): #function to convert frames obtained from video into ascii images
            if img is None:
                img = self.img
            scale_factor = self.scale_factor
            #scale_factor control the dimensions of our output image, more the scale factor larger will be frame window for output image
                       
            Font = ImageFont.truetype('C:\\Windows\\Fonts\\Arial.ttf', 15)#selecting font 
            charwidth, charheight = Font.getsize("A") #width and height of character is chosen from a letter

            width,height=img.size #getting dimensions of original image frame
            #resizing image frame
            new_width = scale_factor*width #defining new_width of image to scale it
            new_height = scale_factor*height*(charwidth/charheight) #new height of image, multiplying with (charwidth/charheight) helps maintain a proper ratio to fit in characters
            img= img.resize((int(new_width),int(new_height)))#resizing image
            new_width,new_height=img.size #we get the output height and width which we will be working on to get access to pixel value
            pixel=img.load()
            bg_code = (0,0,0) if self.bg is True else (255,255,255)#defining bg_code according to bool value of bg as mentioned above
            img=Image.new("RGB",(charwidth*new_width,charheight*new_height),color=bg_code) #creating output image dimensions, bg color
            draw=ImageDraw.Draw(img) 
        #the below loop iterates over new_height, new_width to get pixel values at (j,i) location
        #the pixVal gives a single pixel value based on the luminosity operation
            for i in range(new_height):
                for j in range(new_width):
                    red,green,blue=pixel[j,i]
                    pixVal=int(0.22*red+0.70*green+0.08*blue)#we select a character based on this value using Get_character function
                    draw.text((j*charwidth,i*charheight),self.Get_character(pixVal),font=Font,fill=(red,green,blue))
                    #the character which itself consist of a no. of fixel is assigned the color based on previous pixel
                    #as for every pixel we are assigning a character the size of output image is (charwidth*new_width,charheight*new_height) as selected above
            return img 

    def Get_character(self,p): #to get character based on pixVal value obtained
        charlist=list(self.style)
        charlen=len(charlist)
        return charlist[math.floor(p*charlen/256)] 

    def reverse_bg(self): #reverses bg and ascii sequence to match with bg if we toggle the bg
        self.bg = not self.bg
        self.style = self.style[::-1]

    def video(self): #function that takes video
        cap=cv2.VideoCapture(0) #opens the webcam
        print("Instructions:\n"
              "* Press \'q\' at any time to quit video\n"
              "*Press \'+\' or \'-\' to increase or decrease frame window\n"
              "* Press \'s\' or \'c\' to change ASCII style from current style\n"
              "* Toggle dark mode by pressing \"d\"")
        #loop to continuosly read input video feed and give sequence of output images 
        while True:
            _,img=cap.read() #to read the video
            img=Image.fromarray(img) 

            output=np.array(self.imagify(img))#getting output video(array of frames based on video/webcam feed)
            key=cv2.waitKey(1)
            if key == ord("q"):
                break
            elif key ==ord('s'):
                self.style = "standard"
            elif key ==ord('c'):
                self.style = "complex"
            elif key ==ord("t"):
                self.style = "test"
            elif key == ord('d'): #reverses bg
                self.reverse_bg()
            elif key == ord('+'): #increase window size
                self.scale_factor +=0.01
            elif key == ord('-'):
                self.scale_factor -=0.01#decrease window size
            #using the above keys we can see the changes in our video in real time

            cv2.imshow("AScii Art",output)
        cap.release()
        cv2.destroyAllWindows()

#main function to call video feed
if __name__ == "__main__":
    convert = Video_to_ASCII( bg=True)
    convert.video()
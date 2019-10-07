from PIL import Image
import cv2
def get_main_color(img):
    colors = img.getcolors(2560) #put a higher value if there are many colors in your image
    max_occurence, most_present = 0, 0
    try:
        for c in colors:
            if c[0] > max_occurence:
                (max_occurence, most_present) = c
        return most_present
    except TypeError:
        raise Exception("Too many colors in the image")
def get_avg_color(img):
    red, green, blue = 0, 0, 0
    n = len(img)*len(img[0])
    for row in img:
        for pixel in row:
            print(pixel[0])
            red += pixel[0]
            green += pixel[1]
            blue += pixel[2]
            #print(pixel)
    red = red/n
    green = green / n
    blue = blue / n
    print(red,green,blue)
#img = cv2.imread("Photo1.jpg")
#get_avg_color(img)
def imposition(img1,img2):
    im1 = img1
    im2 = img2
    im1.paste(im2, (j,i), im2)
    Photosave=im1
img = Image.open("Photo1.jpg")
img2 = Image.open("Photo2.jpg")
imgwidth, imgheight = img.size
#img.crop((30, 30, w-80, h-40)).save("file.png")
amount = 1;
width, length = 50, 50
img3 = Image.new("RGBA", (220, 220), (255, 255, 255)) 
img3 = Image.open("redd-11.png").convert("RGBA")
img3 = img3.resize((width,length), Image.ANTIALIAS)
img3.save("red.png")
Photosave=Image.open("Photo1.jpg")
Photosave2=Image.open("Photo2.jpg")
for i in range(0,imgheight,length):
    for j in range(0,imgwidth,width):
        if j+width > imgwidth:
            w = imgwidth
        else:
            w = j+width
        if i+length > imgheight:
            h = imgheight
        else:
            h = i+length
        
        #img.crop((j, i, w, h)).save("images/file"+str(amount)+".png")
        cropimages1=img.crop((j, i, w, h))
        cropimages2=img2.crop((j, i, w, h))
        color1 =  get_avg_color(cropimages1)
        color2 =  get_avg_color(cropimages2)
        mult = abs(color1[0]-color2[0]) * abs(color1[1]-color2[1]) * abs(color1[2]-color2[2])
        print(mult)
        if not(mult<=125000):
            imposition(Photosave,img3)
            imposition(Photosave2,img3)
            cropimages1.save("uncommon/"+"(1)"+str(amount)+str(color1)+".jpg")
            cropimages2.save("uncommon/"+"(2)"+str(amount)+str(color2)+".jpg")
        amount=amount+1
image1 = Photosave
image2 = Photosave2
(width1, height1) = image1.size
(width2, height2) = image2.size
result_width1 = width1+width2
result_height1 = max(height1,height2)
result1=Image.new('RGB', (result_width1, result_height1))
result1.paste(im=image1, box=(0,0))
result1.paste(im=image2, box=(width2,0))
result1.save("resultall.jpg")




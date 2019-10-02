from PIL import Image
def get_main_color(img):
    colors = img.getcolors(256000) #put a higher value if there are many colors in your image
    max_occurence, most_present = 0, 0
    try:
        for c in colors:
            if c[0] > max_occurence:
                (max_occurence, most_present) = c
        return most_present
    except TypeError:
        raise Exception("Too many colors in the image")

img = Image.open("Photo1.jpg")
img2 = Image.open("Photo2.jpg")
imgwidth, imgheight = img.size
#img.crop((30, 30, w-80, h-40)).save("file.png")
amount = 1;
width, length = 70, 70

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
        color1 = get_main_color(cropimages1)
        color2 = get_main_color(cropimages2)
        if not(abs(color1[0]-color2[0])<=50 and abs(color1[1]-color2[1])<=50 and abs(color1[2]-color2[2])<=50 ):
            cropimages1.save("uncommon/"+"(1)"+str(amount)+str(color1)+".jpg")
            cropimages2.save("uncommon/"+"(2)"+str(amount)+str(color2)+".jpg")
        amount=amount+1

       


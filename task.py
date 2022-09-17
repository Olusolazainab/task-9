from PIL import Image

basewidth = 300
img = Image.open('medplus-awolowo.jpg')
wpercent = (basewidth / float(img.size[0]))
hsize = int((float(img.size[1]) * float(wpercent)))
img = img.resize((basewidth, hsize), Image.ANTIALIAS)
img.save('resized_image.jpg')

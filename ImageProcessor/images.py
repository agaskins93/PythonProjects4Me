from PIL import Image, ImageFilter

img = Image.open('./Pokedex/pikachu.jpg')
filtered_img = img.convert('L')
region = filtered_img.crop(box=(100,100,400,400))
#filtered_img.show() show image in dailog box
#turned = filtered_img.rotate(45)
#resize = turned.resize((700,700),3)
#region = resize.crop((.1,.1,.1,.1))
#region.save("grey.png",'png')


img = Image.open('./Pokedex/GarField.JPG')
img.thumbnail((400,200))
img.save('Garfield2.0.jpg')
print(img.size)



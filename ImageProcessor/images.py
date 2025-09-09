from PIL import Image, ImageFilter

img = Image.open('./Pokedex/pikachu.jpg')
filtered_img = img.convert('L')
#filtered_img.show() show image in dailog box
turned = filtered_img.rotate(45)
turned.save("grey.png",'png')




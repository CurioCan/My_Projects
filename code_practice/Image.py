from PIL import Image
mac = Image.open('/home/charitha/Jupyter/14-Working-with-Images/examples.jpg')
type(mac)
mac.show()

def image2_show():
    nature = Image.open('wallpaper.jpg')
    nature.show()

image2_show()


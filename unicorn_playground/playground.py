import time
import signal
from PIL import Image, ImageDraw, ImageFont
from unicorn_hat_sim import unicornhathd


unicornhathd.brightness(0.5)


# https://icomoon.io/app/#/select/image

def draw_icon(image):
    width, height = unicornhathd.get_shape()
    for x in range(width):
        for y in range(height):
            pixel = image.getpixel((y,x))
            r, g, b = int(pixel[0]),int(pixel[1]),int(pixel[2])
            unicornhathd.set_pixel(x, y, r, g, b)

    unicornhathd.show()

try:
    while True:
        img = Image.open('smile.png')
        draw_icon(img)
        time.sleep(0.5)

except KeyboardInterrupt:
    unicornhathd.off()


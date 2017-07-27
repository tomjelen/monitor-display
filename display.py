import time
import unicornhathd
from PIL import Image, ImageDraw, ImageFont

NEUTRAL = tuple([50, 50, 200])
RED = tuple([255, 0, 0])

def init():
    print('initializing..')
    unicornhathd.clear()
    unicornhathd.rotation(270)
    unicornhathd.brightness(1.0)
    scroll_text("Hola! Hola! Hola! Hola!", NEUTRAL)
    unicornhathd.brightness(0.5)

def off():
    print('shutting down..')
    scroll_text('Bye..', NEUTRAL)
    unicornhathd.off()

def show_success():
    print(':)')
    draw_image(Image.open('smile.png'))

def show_failure():
    print(':(')
    unicornhathd.set_all(255, 0, 0)
    unicornhathd.show()

def show_general_failure(message):
    print(message)
    scroll_text(message, RED)
    unicornhathd.set_all(255, 0, 0)
    unicornhathd.show()



def scroll_text(line, color):
    FONT = ("/usr/share/fonts/truetype/freefont/FreeSansBold.ttf", 12)
    font_file, font_size = FONT
    font = ImageFont.truetype(font_file, font_size)

    width, height = unicornhathd.get_shape()
    line_width, _ = font.getsize(line)
    text_width = line_width + width * 2

    image = Image.new("RGB", (text_width, width), (0, 0, 0))
    draw = ImageDraw.Draw(image)
    draw.text((width, 0), line, color, font=font)

    for scroll in range(text_width - width):
        for x in range(width):
            for y in range(height):
                pixel = image.getpixel((x+scroll, y))
                r, g, b = [int(n) for n in pixel]
                unicornhathd.set_pixel(width-1-x, y, r, g, b)

        unicornhathd.show()
        time.sleep(0.01)

def draw_image(image):
    width, height = unicornhathd.get_shape()
    for x in range(width):
        for y in range(height):
            pixel = image.getpixel((x, y))
            r, g, b = int(pixel[0]),int(pixel[1]),int(pixel[2])
            unicornhathd.set_pixel(x, y, r, g, b)

    unicornhathd.show()

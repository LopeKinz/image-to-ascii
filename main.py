from PIL import Image

pic = input("Drag and Drop your image here : ")

# Lade das Bild und konvertiere es in Schwarzweiß
img = Image.open(pic).convert('L')

# Definiere die ASCII-Zeichen, die für das Bild verwendet werden sollen
ascii_chars = [' ', '.', ':', '-', '=', '+', '*', '#', '%', '@']

# Erstelle eine leere Zeichenfolge für das ASCII-Bild
ascii_image = ''

# Iteriere über jedes Pixel im Bild und füge das entsprechende ASCII-Zeichen zur ascii_image-Zeichenfolge hinzu
for y in range(img.size[1]):
    for x in range(img.size[0]):
        pixel_intensity = 255 - img.getpixel((x,y))
        ascii_image += ascii_chars[pixel_intensity // 25]
    ascii_image += '\n'

# Drucke das ASCII-Bild
print(ascii_image)

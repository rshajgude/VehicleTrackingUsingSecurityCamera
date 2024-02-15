
import PIL
import string
import easyocr
import cv2 as cv
import pytesseract

PIL.Image.ANTIALIAS = PIL.Image.LANCZOS

reader = easyocr.Reader(['en'], gpu=False)

filename = 'frame_plate_0_5.jpg'
image = cv.imread(filename)
print(image)

custom_config = r'--oem 3 --psm 6'
result=pytesseract.image_to_string(image, config=custom_config)
print(result)

detection = reader.readtext(image)

img = cv.imread('frame_plate_0_5.jpg')
result = reader.readtext(img)
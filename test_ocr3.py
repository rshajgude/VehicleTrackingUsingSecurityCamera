import os
import easyocr
import cv2
from matplotlib import pyplot as plt
import numpy as np

IMAGE_PATH = 'https://blog.aspose.com/wp-content/uploads/sites/2/2020/05/Perform-OCR-using-C.jpg'
#IMAGE_PATH = 'Perform-OCR.jpg'

reader = easyocr.Reader(['en'])
print("Started")
result = reader.readtext(IMAGE_PATH,paragraph="False")
print(result)
print(type(result))

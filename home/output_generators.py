import cv2 as cv
from pytesseract import pytesseract

def convert_image_to_text(image_path):
	pytesseract.tesseract_cmd = '/usr/bin/tesseract'
	image = cv.imread(image_path)
	#try:
	text = pytesseract.image_to_string(image)
	#except:
	#	text = "Error with the input image!"
	return text 

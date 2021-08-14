import cv2 as cv
from pytesseract import pytesseract
from sympy import *
from wordcloud import WordCloud
from secrets import token_hex
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent

def convert_image_to_text(image_path):
	pytesseract.tesseract_cmd = '/usr/bin/tesseract'
	image = cv.imread(image_path)
	try:
		text = pytesseract.image_to_string(image)
	except:
		text = "Error with the input image!"
	return text 

def find_roots_of_polynomial_eq(eq):
	roots = ""
	try:
		roots_list = solve(eq)
		roots = "All roots of eq - " + eq + " are-\\n"
		for i in range(len(roots_list)):
			roots += str(i+1) + ') ' + str(roots_list[i]) + "\\n"
	except:
		roots = "Error with the equation"
	return roots


def convert_text_to_cloud(text):
	wordcloud = str(token_hex(6)) + ".jpg"
	tmp_wordcloud = WordCloud(background_color="white").generate(text)
	tmp_wordcloud.to_file(str(BASE_DIR/'media'/wordcloud))
	return wordcloud
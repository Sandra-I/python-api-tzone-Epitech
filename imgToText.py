import pytesseract as tess
tess.pytesseract.tesseract_cmd = r'C:\Users\rkane\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'
import cv2
import numpy as np
from PIL import Image
	

#image = cv2.imread("C:/Users/rkane/OneDrive/Bureau/TZone_python/imgToText/testcopy.jpg")
#gray = cv2.cvtColor(image,cv2.COLOR_RGB2GRAY)
#ret2,th2 = cv2.threshold(gray,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
#dst = cv2.fastNlMeansDenoising(th2,10,10,7)
#cv2.imwrite('C:/Users/rkane/OneDrive/Bureau/TZone_python/imgToText/testcopy.jpg',dst)
#img = Image.open('C:/Users/rkane/OneDrive/Bureau/TZone_python/imgToText/lorm.jpg')
#text = tess.image_to_string(image)
#print(text)

def process_image(path):

	#gray = cv2.cvtColor(image,cv2.COLOR_RGB2GRAY)
	#ret2,th2 = cv2.threshold(gray,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
	#dst = cv2.fastNlMeansDenoising(th2,10,10,7)
	#cv2.imwrite('./uploads/tmp.jpg',dst)
	#cao = Image.open('./uploads/tmp.jpg')
	#print ("Recongizeing...")
	#rec_string =  tess.image_to_string(cao,lang='chi_sim')
	#print ("the result is {}".format(rec_string))
 	#return rec_string
	image = cv2.imread(path)
	gray = cv2.cvtColor(image,cv2.COLOR_RGB2GRAY)
	ret2,th2 = cv2.threshold(gray,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
	dst = cv2.fastNlMeansDenoising(th2,10,10,7)
	cv2.imwrite(path,dst)
	#img = Image.open('C:/Users/rkane/OneDrive/Bureau/TZone_python/imgToText/lorm.jpg')
	text = tess.image_to_string(image)
	#return text
	return text


#process_image("C:/Users/rkane/OneDrive/Bureau/TZone_python/imgToText/lorm.jpg")
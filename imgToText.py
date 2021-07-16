import pytesseract as tess
# tess.pytesseract.tesseract_cmd = r'C:\Users\rkane\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'
from PIL import Image

def process_image(path):
	# image = cv2.imread(path)
	# gray = cv2.cvtColor(image,cv2.COLOR_RGB2GRAY)
	# ret2,th2 = cv2.threshold(gray,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
	# dst = cv2.fastNlMeansDenoising(th2,10,10,7)
	# cv2.imwrite(path,dst)
	img = Image.open(path)
	text = tess.image_to_string(img)
	return text

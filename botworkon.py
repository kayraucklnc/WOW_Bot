import cv2
import pytesseract
import numpy as np
import pyautogui


def work():
    pytesseract.pytesseract.tesseract_cmd = r"C:\Users\Kayra\AppData\Local\Tesseract-OCR\tesseract.exe"

    # Load image, grayscale, Otsu's threshold
    im = cv2.imread('2.jpg')
    image = im[900:1400,130:518+90]
    original = image.copy()
    mask = np.zeros(image.shape, dtype=np.uint8)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

    # Find contours and filter using aspect ratio and area
    cnts = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = cnts[0] if len(cnts) == 2 else cnts[1]
    for c in cnts:
        area = cv2.contourArea(c)
        x,y,w,h = cv2.boundingRect(c)
        ar = w / float(h)
        if area > 1000 and ar > .85 and ar < 1.2:
            cv2.rectangle(image, (x, y), (x + w, y + h), (50,50,255), 2)
            cv2.rectangle(mask, (x, y), (x + w, y + h), (0,255,0), -1)
            ROI = original[y:y+h, x:x+w]

    # Bitwise-and to isolate characters
    result = cv2.bitwise_and(original, mask)
    result[mask==0] = 255

    # OCR
    data = pytesseract.image_to_string(result, lang='eng',config='--psm 6').replace(" ","").replace("\n","")
    for i in [0,2,4,5,3,1]:
        print(data[i])

    cv2.imshow('image', image)
    cv2.imshow('thresh', thresh)
    cv2.imshow('result', result)
    cv2.waitKey()

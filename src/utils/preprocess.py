import cv2
import numpy as np
import pytesseract
from PIL._imaging import display

import settings


def pre_process_image(input_image):
    image_array = np.asarray(bytearray(input_image.read()), dtype='uint8')
    image = cv2.imdecode(image_array, cv2.IMREAD_GRAYSCALE)
    image = cv2.dilate(image, (1, 1), iterations=4)
    image = cv2.erode(image, (1, 1), iterations=3)
    ret, thresh_bin = cv2.threshold(image, 135, 250, cv2.THRESH_BINARY)
    processed_image = 250 - thresh_bin
    cv2.imwrite(str(settings.BASE_DIR.parent / "file.png"), processed_image)
    first_digit_image = processed_image[:, int((processed_image.shape[0] * 6) / 9):int((processed_image.shape[1] * 1.1)/ 3)]
    #first_digit_image = cv2.dilate(first_digit_image, (1, 1), iterations=1)
    #first_digit_image = cv2.erode(first_digit_image, (1, 1), iterations=4)
    last_third_digit = processed_image[:, int(((processed_image.shape[0] * 7) / 9)*0.85):int(((processed_image.shape[1] * 18) / 20)*1.1)]
    last_third_digit = cv2.dilate(last_third_digit, (1, 1), iterations=1)
    last_third_digit = cv2.erode(last_third_digit, (1, 1), iterations=2)
    last_third_digit = cv2.dilate(last_third_digit, (1, 1), iterations=0)
    last_third_digit = cv2.resize(last_third_digit, dsize=(200, 120))
    cv2.imwrite("first_digit_image.png", first_digit_image)
    cv2.imwrite("trim_image.png", last_third_digit)
    return last_third_digit

def get_text_from_clear_image_numeric(clear_image):
    text = pytesseract.image_to_string(clear_image, lang='eng')
    text = "".join([i for i in text if i.isnumeric()])
    return text


def get_text_from_clear_image_alphanumeric(clear_image):
    text = pytesseract.image_to_string(clear_image, lang='eng')
    text = "".join([i for i in text if i.isalnum()])
    return text

import cv2
import numpy as np
import pytesseract

import settings


def pre_process_image(input_image):
    image_array = np.asarray(bytearray(input_image.read()), dtype='uint8')
    image = cv2.imdecode(image_array, cv2.IMREAD_GRAYSCALE)
    image = cv2.dilate(image, (1, 1), iterations=5)
    ret, thresh_bin = cv2.threshold(image, 160, 255, cv2.THRESH_BINARY)
    processed_image = 255 - thresh_bin
    cv2.imwrite(str(settings.BASE_DIR.parent / "file.png"), processed_image)
    return processed_image
    # first_digit = processed_image[:, int(processed_image.shape[0] / 9) * 5:int((processed_image.shape[1] * 1) / 3)]
    # second_digit = processed_image[:, int((processed_image.shape[0] * 2) / 9) :int((processed_image.shape[1] * 2) / 3)]
    # thrid_digit = processed_image[:, int((processed_image.shape[0] * 12) / 11):int((processed_image.shape[1] * 3) / 3)]
    # fourth_digit = processed_image[:, int((processed_image.shape[0] * 2) / 9):int((processed_image.shape[1] * 4) / 3)]

    # cv2.imwrite("first_digit.png", first_digit)
    # cv2.imwrite("second_digit.png", second_digit)
    # cv2.imwrite("third_digit.png", thrid_digit)
    # cv2.imwrite("fouth_digit.png", fourth_digit)
    # print(get_text_from_clear_image_numeric(first_digit))


def get_text_from_clear_image_numeric(clear_image):
    text = pytesseract.image_to_string(clear_image, lang='eng')
    text = "".join([i for i in text if i.isnumeric()])
    return text


def get_text_from_clear_image_alphanumeric(clear_image):
    text = pytesseract.image_to_string(clear_image, lang='eng')
    text = "".join([i for i in text if i.isalnum()])
    return text

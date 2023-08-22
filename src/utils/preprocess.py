import cv2
import numpy as np
import pytesseract
import settings


def pre_process_image(input_image):
    image_array = np.asarray(bytearray(input_image.read()), dtype='uint8')
    image = cv2.imdecode(image_array, cv2.IMREAD_GRAYSCALE)
    image = cv2.dilate(image, (1, 1), iterations=3)
    image = cv2.erode(image, (1, 1), iterations=0)
    # image = cv2.dilate(image, (1, 1), iterations=1)
    ret, thresh_bin = cv2.threshold(image, 160, 255, cv2.THRESH_BINARY)
    processed_image = 255 - thresh_bin
    cv2.imwrite(str(settings.BASE_DIR.parent / "file.png"), processed_image)
    first_digit_image = processed_image[:,
                        int((processed_image.shape[0] * 6) / 9):int((processed_image.shape[1] * 1.1) / 3)]
    first_digit_image = cv2.dilate(first_digit_image, (1, 1), iterations=2)
    first_digit_image = cv2.erode(first_digit_image, (1, 1), iterations=3)
    ret, thresh_bin = cv2.threshold(first_digit_image, 130, 245, cv2.THRESH_BINARY)
    first_digit_image = 255 - thresh_bin

    trim_image = processed_image[:, int(((processed_image.shape[0] * 7) / 9) * 2.2):int(
        ((processed_image.shape[1] * 2) / 7) * 1.8)]
    trim_image = cv2.dilate(trim_image, (1, 1), iterations=3)
    ret, thresh_bin = cv2.threshold(trim_image, 160, 255, cv2.THRESH_BINARY)
    trim_image = 255 - thresh_bin

    third_digit = processed_image[:, int(((processed_image.shape[0] * 2) / 9) * 8):int(
        ((processed_image.shape[1] * 2) / 7) * 2.7)]
    third_digit = cv2.dilate(third_digit, (1, 1), iterations=3)
    ret, thresh_bin = cv2.threshold(third_digit, 160, 255, cv2.THRESH_BINARY)
    third_digit = 255 - thresh_bin

    fourth_digit = processed_image[:, int(((processed_image.shape[0] * 2) / 9) * 11.6):int(
        ((processed_image.shape[1] * 2) / 7) * 4.5)]
    fourth_digit = cv2.dilate(fourth_digit, (1, 1), iterations=3)
    ret, thresh_bin = cv2.threshold(fourth_digit, 160, 255, cv2.THRESH_BINARY)
    fourth_digit = 255 - thresh_bin

    cv2.imwrite("first_digit_image.png", first_digit_image)
    cv2.imwrite("second_digit.png", trim_image)
    cv2.imwrite("third_digit.png", third_digit)
    cv2.imwrite("fourth_digit.png", fourth_digit)
    return third_digit


def get_text_from_clear_image_numeric(clear_image):
    text = pytesseract.image_to_string(clear_image, lang='eng')
    text = "".join(([i for i in text if i.isnumeric()]))
    return text


def get_text_from_clear_image_alphanumeric(clear_image):
    text = pytesseract.image_to_string(clear_image, lang='eng')
    text = "".join([i for i in text if i.isalnum()])
    return text

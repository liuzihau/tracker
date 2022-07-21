import cv2


def binary_threshold(image, thres=128, value=255):
    if len(image.shape) == 3:
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return cv2.threshold(image, thres, value, cv2.THRESH_BINARY)

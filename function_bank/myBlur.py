import cv2


def gaussian(image, kernel=[3, 3], sigma=0):
    kernel = [v+1 if v % 2 == 0 else v for v in kernel]
    return cv2.GaussianBlur(image, kernel, sigma)

import numpy as np
import cv2


def canny_higher(image, threshold=10, r=3, kernel_size=3):
    detected_edges = cv2.Canny(image, threshold, threshold * r, apertureSize=kernel_size)
    return detected_edges


def percentage_canny(image, percentage=90):
    quantile = np.percentile(image, percentage)
    return canny_higher(image, int(quantile), r=3, kernel_size=3)

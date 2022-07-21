import cv2
import numpy as np


# 指定颜色替换
def fill_image(image,
               start_point: tuple = (0, 0),
               color: tuple = (255, 255, 255),
               loDiff: tuple = (100, 100, 50),
               upDiff: tuple = (50, 50, 50)):
    copyImage = image.copy()
    h, w = image.shape[:2]
    mask = np.zeros([h + 2, w + 2], np.uint8)  # make a new array as mask array, +2 is request from official
    '''
    seedPoint: 起始測試點.

    newVal:通過測試的pixel要填入的值

    loDiff:與相鄰像素能容忍的最大差異下限

    upDiff:與相鄰像素能容忍的最大差異上限

    '''
    cv2.floodFill(copyImage, mask, start_point, color, loDiff, upDiff,
                  flags=4 | (255 << 8) | cv2.FLOODFILL_FIXED_RANGE)
    mask_copy = mask[1:h + 1, 1:w + 1]  # 1~h 1~w 對應原圖的 0~h-1 0~w-1
    mask_copy = cv2.merge([mask_copy, mask_copy, mask_copy])  # merge to create 3 channel
    mask = cv2.bitwise_and(image, mask_copy)  # mask不為0的地方(被漫水填充的地方)才會show出來

    return copyImage, mask


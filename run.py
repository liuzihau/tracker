from script_code.helper import *
from script_code.function_manager import FunctionManager
from script_code.tracker import Tracker
import cv2

from function_bank.myBlur import gaussian
from function_bank.myCanny import percentage_canny
from function_bank.myFloodfill import fill_image


def run(opt):
    fn_mgr = FunctionManager(opt, [gaussian,percentage_canny])#fill_image, percentage_canny])
    image = cv2.imread(opt.source_file)
    res = fn_mgr.script()
    tracker = Tracker(image, res)
    tracker.track()


if __name__ == '__main__':
    path = './setting/config.yaml'
    opt = get_config(path)
    run(opt)

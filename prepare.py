from script_code.helper import *
from script_code.function_manager import FunctionManager

from function_bank.myBlur import gaussian
from function_bank.myCanny import percentage_canny
from function_bank.myFloodfill import fill_image


def prepare(opt):
    fn_mgr = FunctionManager(opt, [gaussian,percentage_canny])#fill_image, percentage_canny])
    fn_mgr.output_json_script()


if __name__ == '__main__':
    path = './setting/config.yaml'
    opt = get_config(path)
    prepare(opt)

from inspect import signature
import json
from script_code.helper import *


class FunctionManager(object):
    def __init__(self, opt, fn_list):
        self.opt = opt
        self.fn_list = fn_list

    def output_json_script(self):
        parameter_list = self.extract_parameter()
        self.export_json_file(parameter_list)

    def script(self):
        parameter_list = self.import_json_file()
        return zip(parameter_list, self.fn_list)

    def extract_parameter(self):
        parameter_list = []
        for fn in self.fn_list:
            sig = signature(fn)
            fn_dict = {p.name: p.default if type(p.default) != type else None for p in sig.parameters.values() if
                       p.kind == p.POSITIONAL_OR_KEYWORD}
            fn_dict['fn_name'] = fn.__name__
            parameter_list.append(fn_dict)
        return parameter_list

    def export_json_file(self, parameter_list):
        with open(self.opt.script_file_path, 'w', encoding='utf-8') as f:
            json.dump(parameter_list, f, indent=4, ensure_ascii=False)

    def import_json_file(self):
        with open(self.opt.script_file_path, 'r', encoding='utf-8') as f:
            return json.loads(f.read())


if __name__ == '__main__':
    from function_bank.myCanny import percentage_canny
    from function_bank.myFloodfill import fill_image

    path = './setting/config.yaml'
    fn_mgr = FunctionManager(get_config(path), [percentage_canny, fill_image])
    fn_mgr.output_json_script()
    res = fn_mgr.script()
    for i, v in res:
        print(i, v)

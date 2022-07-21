from functools import partial
import cv2


def create_windows(window_name, para_counts):
    window_width = 400
    window_height = 150 + 50 * para_counts
    cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
    cv2.resizeWindow(window_name, window_width, window_height)


def package_parameter(up, parameter):
    for key in up:
        split_list = key.split('|')
        if key in parameter:
            parameter[key] = up[key]
        elif split_list[0] in parameter:
            parameter[split_list[0]][int(split_list[1])] = up[key]


class Tracker(object):
    def __init__(self, image, fn):
        self.input_image = image
        self.window_name = 'show'
        packed_list = []
        unpacked_list = []
        fn_list = []
        fn_name_list = []
        # unpacked_list
        for p, f in fn:
            p.pop('image')
            fn_name_list.append(p.pop('fn_name'))
            packed_list.append(p)
            # p['image']=input_image
            # windows_name = p.pop('fn_name')
            fn_list.append(f)
            fn_unpack_dict = {}
            for key in p:
                if key in ['image', 'img', 'fn_name']:
                    continue
                if hasattr(p[key], '__len__') and type(p[key]) != str:
                    for i, parameter in enumerate(p[key]):
                        fn_unpack_dict[f'{key}|{i}'] = parameter
                else:
                    fn_unpack_dict[f'{key}'] = p[key]
            unpacked_list.append(fn_unpack_dict)
        self.packed_list = packed_list
        self.unpacked_list = unpacked_list
        self.fn_name_list = fn_name_list
        self.fn_list = fn_list

    def track(self):
        for i, fn in enumerate(self.fn_list):
            create_windows(self.fn_name_list[i], len(self.unpacked_list[i]))
            for key in self.unpacked_list[i]:
                split_key = key.split('|')
                p_idx = split_key[1] if len(split_key)>1 else None
                fn = partial(self.work_function, fn_idx=i, p_name=split_key[0], p_idx=p_idx)
                cv2.createTrackbar(key, self.fn_name_list[i],
                                   self.unpacked_list[i][key], 100, fn)
        if cv2.waitKey(0) == 27:
            cv2.destroyAllWindows()

    def work_function(self, value, fn_idx, p_name, p_idx):
        x = self.input_image
        for i, fn in enumerate(self.fn_list):
            target_p = self.unpacked_list[i]
            if i == fn_idx:
                if f'{p_name}|{p_idx}' in target_p:
                    target_p[f'{p_name}|{p_idx}'] = value
                elif p_name in target_p:
                    target_p[p_name] = value
            package_parameter(target_p, self.packed_list[i])
            x = fn(image=x, **self.packed_list[i])
            if type(x) == tuple:
                x = x[0]
        cv2.imshow(self.window_name, x)

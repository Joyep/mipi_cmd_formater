from fmt_rk3399 import Format3399
from fmt_rk3288 import Format3288
from fmt_qcom_dts import FormatQcomDTS
from fmt_qcom_lk import FormatQcomLK
from fmt_qcom_lk2 import FormatQcomLK2

supported_fmts = {
    '3399': (Format3399(),),
    '3288': (Format3288(),),
    'qcomdts': (FormatQcomDTS(),),
    'qcomlk': (FormatQcomLK(), FormatQcomLK2()),
}


class Formater(object):

    def __init__(self, format_name):
        self.fmt = supported_fmts.get(format_name, None)

    def valid(self):
        return self.fmt != None

    def get_fmt_type(self):
        return self.fmt[0].get_fmt_type()

    def format(self, data):

        if not self.valid():
            print("format not support!")
            return

        lines = []
        for f in self.fmt:
            lines = lines + f.format(data)

        return lines


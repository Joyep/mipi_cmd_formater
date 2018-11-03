
from functools import reduce

def append_list(l1, l2):
    return l1 +l2

class Format(object):

    def format(self, data):
        # Data format:
        #   data = {'name': 'lcd_name', 'cmd_list': cmd_list}
        #   cmd_list = [(dtype, cmds[], delay_ms, index),...]
        if 0 == len(data['cmd_list']):
            print("cmd list is empty")
            return
        self.data = data
        return self.format_head() + reduce(append_list, (map(self.format_cmd, data['cmd_list']))) + self.format_foot()

    def format_head(self):
        pass
    def format_foot(self):
        pass
    def format_cmd(self, cmd):
        pass

    def get_fmt_type(self):
        return "undefined"
    def get_fmt_suffix(self):
        return "txt"

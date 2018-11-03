from fmt_base import Format

T1 = "\t"
T2 = "\t"
T3 = "\t"

#lk cmd item format
lk_cmd_start =  "static char %s_on_cmd%d[] = {\n"
lk_cmd_cnt =    T1 + "0x%02X, 0x00, 0x39, 0xC0,\n"
lk_cmd =        T1 + "0x%02X, 0x%02X, 0x%02X, 0x%02X,\n"
lk_cmd_end =    "};\n\n"

def format_lk_cmds(cmd):
    #other params
    p_grp = [0xff, 0xff, 0xff, 0xff] #四个参数一组
    lk_item_lines = []

    p_index = 0
    for param in cmd: #遍历命令参数列表
        p_grp[p_index] = param
        p_index = (p_index+1) % 4
        if p_index == 0: #满了一组
            l = lk_cmd % (p_grp[0], p_grp[1], p_grp[2], p_grp[3])
            lk_item_lines.append(l)
            #p_lines += 1

    if p_index != 0:  #组还有剩余, 填充FF
        while p_index < 4:
            p_grp[p_index] = 0xff
            p_index += 1
        l = lk_cmd % (p_grp[0], p_grp[1], p_grp[2], p_grp[3])
        lk_item_lines.append(l)
        #p_lines += 1

    return lk_item_lines


class FormatQcomLK(Format):

    def format_head(self):
        return []

    def format_foot(self):
        return []

    def format_cmd(self, cmd):
        #cmd = (dtype, cmds[], delay_ms, index)
        return [
            lk_cmd_start % (self.data['name'], cmd[3]),
            lk_cmd_cnt % (len(cmd[1])),
        ] + format_lk_cmds(cmd[1]) + [lk_cmd_end]

    def get_fmt_type(self):
        return "QCOM_LK_H"

    def get_fmt_suffix(self):
        return "h"

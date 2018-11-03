from fmt_base import Format

T1 = "\t"
lk_cmd_list_name =      "static struct mipi_dsi_cmd %s_on_command[] = {\n"
lk_cmd_list_item =      T1 + "{0x%02X, %s_on_cmd%d, 0x%02X},\n"
lk_cmd_end =            "};\n\n"
lk_cmd_cnt_define =     "#define %s_ON_COMMAND %d"



class FormatQcomLK2(Format):

    def format_head(self):
        return [ lk_cmd_list_name % (self.data['name']) ]

    def format_foot(self):
        return [
            lk_cmd_end,
            lk_cmd_cnt_define % (self.data['name'].upper(), len(self.data['cmd_list'])),
        ]

    def format_cmd(self, cmd):
        #cmd = (dtype, params[], delay_ms, index)

        #get params count, 4 number align
        cnt = len(cmd[1])
        if cnt%4 != 0:
            cnt = cnt + (4-(cnt%4))

        return [
            lk_cmd_list_item % (4+cnt, self.data['name'], cmd[3], cmd[2]),
        ]


    def get_fmt_type(self):
        return "QCOM_LK2_H"

    def get_fmt_suffix(self):
        return "h"


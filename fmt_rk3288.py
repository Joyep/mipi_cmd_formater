from fmt_base import Format

T1 = "\t\t"
T2 = "\t"
T3 = "\t"
fmt_3288_head_1 =     T1 + "screen-on-cmds {\n"
fmt_3288_head_2 =     T1 + T2 + "rockchip,cmd_debug = <0>;\n"
fmt_3288_head_3 =     T1 + T2 + "compatible = \"rockchip,screen-on-cmds\";\n"
fmt_3288_start =      T1 + T2 + "rockchip,on-cmds%d {\n"
fmt_3288_compatible = T1 + T2 + T3 + "compatible = \"rockchip,on-cmds\";\n"
fmt_3288_type =       T1 + T2 + T3 + "rockchip,cmd_type = <LPDT>;\n"
fmt_3288_dsi_id =     T1 + T2 + T3 + "rockchip,dsi_id = <0>;\n"
fmt_3288_cmd =        T1 + T2 + T3 + "rockchip,cmd = <%s>;\n"
fmt_3288_delay =      T1 + T2 + T3 + "rockchip,cmd_delay = <%d>;\n"
fmt_3288_end =        T1 + T2 + "};\n"
fmt_3288_foot =       T1 + "};\n"


class Format3288(Format):

    def format_head(self):
        return [ fmt_3288_head_1, fmt_3288_head_2, fmt_3288_head_3 ]

    def format_foot(self):
        return [ fmt_3288_foot ]

    def format_cmd(self, cmd):
        params = " ".join(["0x%02X" % x for x in cmd[1] ])
        rockchip_cmd = "0x%02X %s" % (cmd[0], params)
        return [
            fmt_3288_start % cmd[3],
            fmt_3288_compatible,
            fmt_3288_type,
            fmt_3288_dsi_id,
            fmt_3288_cmd % rockchip_cmd,
            fmt_3288_delay % cmd[2],
            fmt_3288_end
        ]

    def get_fmt_type(self):
        return "RK3288_DTSI"

    def get_fmt_suffix(self):
        return "dtsi"


from fmt_base import Format

T1 = "\t\t"
T2 = "\t"
dtsi_head =     T1 + "qcom,mdss-dsi-on-command = [\n"
dtsi_fmt =      T1 + T2 + "39 01 00 00 %02X 00 %02X %s\n"
dtsi_end =      T1 + "];\n"

class FormatQcomDTS(Format):

    def format_head(self):
        return [dtsi_head]

    def format_foot(self):
        return [dtsi_end]

    def format_cmd(self, cmd):
        #(dtype, cmds[], delay_ms, index)
        params = " ".join(["%02X" % x for x in cmd[1] ])
        return [ dtsi_fmt % (cmd[2], len(cmd[1]), params)]

    def get_fmt_type(self):
        return "QCOM_DTSI"

    def get_fmt_suffix(self):
        return "dtsi"


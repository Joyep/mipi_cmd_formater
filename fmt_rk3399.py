from fmt_base import Format

fmt_3399_head = "\t\tpanel-init-sequence = [\n"
fmt_3399_cmd =  "\t\t\t%02X %02X %02X %s\n"
fmt_3399_foot = "\t\t];\n"

class Format3399(Format):

    def format_head(self):
        return [ fmt_3399_head ]

    def format_foot(self):
        return [ fmt_3399_foot ]

    def format_cmd(self, cmd):
        cmd_lines = []
        params = " ".join(["%02X" % x for x in cmd[1] ])
        return [fmt_3399_cmd % (cmd[0], cmd[2], len(cmd[1]), params)]

    def get_fmt_type(self):
        return "RK3399_DTSI"

    def get_fmt_suffix(self):
        return "dtsi"

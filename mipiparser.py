
from enum import Enum, unique




def is_invalid_line(line):
    line = line.strip('\r')
    line = line.strip('\n')
    line = line.strip()
    return line.startswith('#') or line.startswith(';') or line.startswith('//') or line == ""

def parse_mipi_cmd(cmd):
    p_arr = cmd.split()
    count = len(p_arr)

    p = p_arr[0]; # get dtype from first param
    if p == "GEN":
        p_arr.pop(0)
        if count == 2: #no param
            dtype = 0x03;
        elif count == 3: #1 param
            dtype = 0x13;
        elif count == 4: #2 param
            dtype = 0x23;
        elif count > 4: #more param
            dtype = 0x29;
    elif p == "DCS":
        p_arr.pop(0)
        if count == 2: #no param
            dtype = 0x05;
        elif count == 3: #1 param
            dtype = 0x15;
        elif count > 3: #more param
            dtype = 0x39;
    else :  #if no dtype, default use DCS
        if count == 1: #no param
            dtype = 0x05;
        elif count == 2: #1 param
            dtype = 0x15;
        elif count > 2: #more param
            dtype = 0x39;

    p_arr = [int(p, 16) for p in p_arr]

    return dtype, p_arr


def parse_line(line):

    valid_cmd = line

    # remove #comment
    tmp_arr = valid_cmd.split("#")
    if len(tmp_arr) != 1:
        valid_cmd = tmp_arr[0].strip()

    #remove //comment
    tmp_arr = valid_cmd.split("//")
    if len(tmp_arr) != 1:
        valid_cmd = tmp_arr[0].strip()

    # get delay if exist
    cmd = valid_cmd
    delay = 0
    tmp_arr = valid_cmd.split("delay")
    if len(tmp_arr) >= 2 :
        cmd = tmp_arr[0].strip()
        delay = int(tmp_arr[1].strip())

    #make cmd upper
    cmd = cmd.upper()

    #split cmd to array
    dtype, p_arr = parse_mipi_cmd(cmd)

    return dtype, p_arr, delay


class Parser(object):

    @unique
    class Version(Enum):
        V1 = 1

    def __init__(self, version):
        self.version = version

    def parse(self, pfile):
         #open pfile, read line by line
        file = open ( pfile, 'r', encoding='UTF-8')
        lines = file.readlines()

        cmd_list = []
        index = 0
        line_index = 0
        for line in lines:
            line_index = line_index + 1
            if is_invalid_line(line):
                continue
            #print(line)
            try:
                dtype, params, delay = parse_line(line)
            except ValueError as e:
                print("parse file error! line:%d" % line_index)
                return
            #print("dtype=0x%x" % dtype)
            #print("params=", params)
            #print("delay=", delay)
            cmd_list.append((dtype, params, delay, index))
            index = index + 1

        print(">>> %d mipi cmd(s) parsed!" % index)
        return cmd_list



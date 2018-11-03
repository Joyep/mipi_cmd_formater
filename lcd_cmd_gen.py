#!/usr/bin/python
# coding=utf-8

import sys
import os

def generate(lcd_name, pfile):

    print "Generating dtsi and lk.h format file for DSI init codes..."
    print "parse file:", pfile
    print "lcd_name:", lcd_name

# out file
    dtsi_file = lcd_name + "_" + pfile + ".dtsi"
    lk_file = lcd_name + "_" + pfile + ".lk.h"
# out lines temp
    dtsi_lines = []
    lk_item_lines = []
    lk_list_lines = []

#format
    dtsi_head = "\t\tqcom,mdss-dsi-on-command = [\n"
    dtsi_end = "\t\t];\n"
    dtsi_fmt = "\t\t\t39 01 00 00 %02X 00 %02X %s\n"
#lk cmd item format
    lk_cmd_start = "static char %s_on_cmd%d[] = {\n"
    lk_cmd_cnt = "\t0x%02X, 0x00, 0x39, 0xC0,\n"
    lk_cmd = "\t0x%s, 0x%s, 0x%s, 0x%s,\n"
    lk_cmd_end = "};\n\n"

#lk cmd list format
    lk_cmd_list_name = "static struct mipi_dsi_cmd %s_on_command[] = {\n"
    lk_cmd_list_item = "\t{0x%02X, %s_on_cmd%d, 0x%02X},\n"
    lk_cmd_cnt_define = "#define %s_ON_COMMAND %d"

#dtsi head
    dtsi_lines.append(dtsi_head)
#lk list head
    l = lk_cmd_list_name % (lcd_name)
    lk_list_lines.append(l)

#start to parse pfile
    params = open ( pfile, 'r' )
    lines = params.readlines()
    index = 0
    for line in lines:
        #print "--------"
        line = line.strip('\r')
        line = line.strip('\n')
        line = line.strip()
        if line.startswith('#'):
            continue
        if line.startswith(';'):
            continue
        if line.startswith('//'):
            continue
        if line == "":
            continue

        # get delay time
        delay = 0
        count = 0

        # remove #comment
        valid_cmd = line
        valid_arr = valid_cmd.split("#")
        if len(valid_arr) != 1:
            valid_cmd = valid_arr[0].strip()

        #remove //comment
        valid_arr = valid_cmd.split("//")
        if len(valid_arr) != 1:
            valid_cmd = valid_arr[0].strip()


        # get delay if exist
        cmd = valid_cmd
        delay_arr = valid_cmd.split("delay")
        if len(delay_arr) >= 2 :
            cmd = delay_arr[0].strip()
            delay = int(delay_arr[1].strip())

        #make cmd upper
        cmd = cmd.upper()
        #print "cmd:", cmd

        #split cmd to array
        p_arr = cmd.split()
        count = len(p_arr)
        #print "count:", count
        #print "delay:", delay

        # got cmd, count and delay
        # we should handle them now

#1, for one dtsi line
        l = dtsi_fmt % (delay, count, cmd)
        dtsi_lines.append(l)

#2, for one lk item
        #item head
        l = lk_cmd_start % (lcd_name, index)
        lk_item_lines.append(l)

        #params
        l = lk_cmd_cnt % (count)
        lk_item_lines.append(l)
        p_lines = 1   #参数的行数

        #other params
        p_grp = ["FF", "FF", "FF", "FF"] #四个参数一组
        p_index = 0
        for param in p_arr: #遍历命令参数列表
            p_grp[p_index] = param
            p_index = (p_index+1) % 4
            if p_index == 0: #满了一组
                l = lk_cmd % (p_grp[0], p_grp[1], p_grp[2], p_grp[3])
                lk_item_lines.append(l)
                p_lines += 1
        if p_index != 0:  #组还有剩余, 填充FF
            while p_index < 4:
                p_grp[p_index] = "FF"
                p_index += 1
            l = lk_cmd % (p_grp[0], p_grp[1], p_grp[2], p_grp[3])
            lk_item_lines.append(l)
            p_lines += 1

        #item end
        lk_item_lines.append(lk_cmd_end)

        #3, for one lk list item
        l = lk_cmd_list_item % (p_lines*4, lcd_name, index, delay)
        lk_list_lines.append(l)

        index += 1
    # end of parse pfile

#dtsi end
    dtsi_lines.append(dtsi_end)

# lk list
    lk_list_lines.append(lk_cmd_end)

# lk list count define
    l = lk_cmd_cnt_define % (lcd_name.upper(), index)
    lk_list_lines.append(l)

# save to file
    dtsi = open ( dtsi_file, 'w' )
    lk = open ( lk_file, 'w' )
    dtsi.writelines(dtsi_lines)
    lk.writelines(lk_item_lines)
    lk.writelines(lk_list_lines)
    dtsi.close();
    lk.close();

    print "dtsi format: ", dtsi_file
    print "lk.h format: ", lk_file
    print "Success!"


#main
#param1: lcd name
#param2: params file, must be as the format as sample file (lcd_params.txt)
lcd_name = sys.argv[1]
params_file = sys.argv[2]
generate(lcd_name, params_file)

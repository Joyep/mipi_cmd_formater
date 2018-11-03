#!/usr/bin/python3
# coding=utf-8

import sys
import os

from mipiformater import Formater
from mipiparser import Parser



def gen(lcd_name, pfile, format_name = '3288'):
    print("Generate formatted mipi cmd file...")

    #new parser and formater
    p = Parser(Parser.Version.V1)
    f = Formater(format_name)
    if not f.valid():
        print("Error: format(%s) not support!" % format_name)
        return

    #parse file
    print("Input File: %s" % pfile)
    cmd_list = p.parse(pfile)
    if not cmd_list:
        print("Error: parse failed!")
        return
    #print(">>> %d mipi cmd(s) parsed!" % len(cmd_list))


    #format
    data = {
        'name': lcd_name,
        'cmd_list': cmd_list,
    }
    print("Output Format: ", f.get_fmt_type())
    formated_lines = f.format(data)
    if not formated_lines:
        print("Error: format result empty!")
        return

    #save to file
    pfilename = os.path.basename(pfile)
    pfilename = pfilename.split('.')[0]
    outfile = "lcd_" + lcd_name + "_" + pfilename +  "_" +  format_name + "." + f.fmt[0].get_fmt_suffix()
    out = open ( outfile, 'w' )
    out.writelines(formated_lines)
    out.close();


    print("Output File: %s" % outfile)
    print("Generate success!\n")


arglen = len(sys.argv)
if(arglen == 3):
    gen(sys.argv[1], sys.argv[2])
elif(arglen == 4):
    gen(sys.argv[1], sys.argv[2], sys.argv[3])

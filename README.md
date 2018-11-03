###mipi cmd formater
	Format mipi cmds for different platform usage.


##Usage
(refer test.sh)
1, write a simple mipi cmd file. (file format see cmds.txt)
2, python3 gen.py <lcd_name> <cmd_file> [format_name]
	lcd_name: any string
	cmd_file: file path of simple mipi cmd file
	format_name: one of 3288, 3399, qcomlk, qcomdts. default format is 3288 if undefined.


##cmds_file format
(see cmds.txt)


##Code Description
#parser.py
	--- simple mipi cmd file parser
#formater.py
	--- target formater, there are some supported format.
#fmt_base.py
	--- Format class
#fmt_xxx.py
	--- FormatXXX extends Format






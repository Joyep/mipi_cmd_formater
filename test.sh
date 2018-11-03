#!/bin/bash

lcdname="abc"

echo ">>>Generate for rk3288 dtsi..."
python3 gen.py $lcdname cmds.txt 3288

echo ">>>Generate for rk3399 dtsi..."
python3 gen.py $lcdname cmds.txt 3399

echo ">>>Generate for qcomdts..."
python3 gen.py $lcdname cmds.txt qcomdts

echo ">>>Generate for qcomlk..."
python3 gen.py $lcdname cmds.txt qcomlk

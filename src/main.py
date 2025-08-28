#!/usr/bin/env python3
#!/bin/python3

from sys import *
from src.preliminary import *
from src.formula import *

#global variable
yellow_color = "\033[1;33m"; white_color = "\033[1;37m"
italic_style = "\x1B[3m"; reset_style = "\033[0m"
day = 0; g = 0; r = 0; s = 0

def loop_projet():
    count = 1; input_user = ""; c_r = 0; n =0; p=0; one = 0; count_switch = 0
    global g, r ,s, temperature_copy, temperature_values, list_g, aberration_values

    while True:
        #take input
        try:
            input_user = input(yellow_color+italic_style)
        except EOFError: #check if stop is not presente
            print(white_color+"Exit(84)\nError No stop, add STOP")
            exit(84)
        print(white_color,end=""); print(reset_style, end="")
        if (input_user == "STOP"): break
        
        #check input and do something
        pointer = 0
        if check_input(input_user):
            temperature_values.append(float(input_user))
            temperature_copy.append(float(input_user))
            temperature_copy_two.append(float(input_user))
            main_control(count, day)
            if count >= day:
                if (len(list_g) >= 6): s = calcul_s()
                if (len(list_g) >= 7):
                    g = calcul_g(day); r = round(calcul_r(day)); c_r+=1
                    #display "a switch occurs" one time (begin)
                    if c_r > 1: one = 1
                    if r < 0: p = 0 ;n += 1 
                    else: n = 0 ;p += 1
                    if (p == 1 and one == 1) or (n == 1 and one == 1):
                        print_output_switch()
                        count_switch+=1
                        pointer = 1
                    #(end)
            else: 
                g = r = s = "nan"
            count +=1
            if pointer == 1: continue
            print_output()
        else: exit(84)
    if count < day: exit(84) #to resolve when there's not enough value
    aberration_values = calcul_aberration_value()
    print(f"Global tendency switched {count_switch} times")
    print(f"5 weirdest values are {aberration_values}")

def print_output():
    print("g="+"%.2f"%float(g)+"\t\t", end="")
    print(f"r={r}%"+"\t\t", end="")
    print("s="+"%.2f"%float(s))

def print_output_switch():
    print("g="+"%.2f"%float(g)+"\t\t", end="")
    print(f"r={r}%"+"\t\t", end="")
    print("s="+"%.2f"%float(s)+"\t\t"+"a switch occurs")

if __name__ == "__main__":
    n = len(argv)
    if n == 2:
        if argv[1] == "-h": help()
        if not argv[1].isdigit(): exit(84)
        day = int(argv[1])
        if day == 0: exit(84)
        loop_projet()
    else: 
        exit(84)
 
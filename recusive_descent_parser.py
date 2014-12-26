__author__ = 'michael'

import pyparsing


def create_string():
    f = open("pars.txt", 'r')

    variable = pyparsing.Word(pyparsing.alphas + pyparsing.nums)
    NaturalNum = pyparsing.Word(pyparsing.nums)
    power = variable + pyparsing.Literal("^") + pyparsing.Literal("(") + pyparsing.nums[2] + \
            pyparsing.Literal("*") + NaturalNum + pyparsing.Literal(")")
    pars_string = power + pyparsing.Literal("+") + power

    input_string = f.readline()
    f.close()
    return pars_string.parseString(input_string)



def generate_of_run_file():
    file_for_running.write("from __future__ import division\n")
    file_for_running.write("x = int(raw_input('Enter the value of X: '))\n")
    file_for_running.write("y = int(raw_input('Enter the value of Y: '))\n")
    file_for_running.write("var1 = %s\n" % create_string()[5])
    file_for_running.write("var2 = %s\n" % create_string()[13])
    file_for_running.write("\n")
    file_for_running.write("print x**(2*var1)+y**(2*var2)")

file_for_running = open("run_me.py", "w")
generate_of_run_file()
file_for_running.close()
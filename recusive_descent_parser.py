__author__ = 'michael'

import pyparsing


def create_string():
    f = open("pars.txt", 'r')
    count = int(f.readline())
    i = count
    variable = pyparsing.Word(pyparsing.alphas + pyparsing.nums)
    fraction = pyparsing.nums[1] + pyparsing.Literal("/") + variable
    pars_string = pyparsing.nums[1]
    while count != 0:
        pars_string = pars_string + pyparsing.Literal("+") + fraction
        count -= 1

    input_string = f.readline()
    print input_string
    f.close()
    print pars_string.parseString(input_string)
    return i, pars_string.parseString(input_string)


def generate_of_run_file(count):
    file_for_running.write("from __future__ import division\n")
    file_for_running.write("count = %s\n" % count)
    file_for_running.write("variable=[]\n")
    file_for_running.write("while count != 0:\n")
    file_for_running.write("\tvariable.append(int(raw_input('Enter the value of variable: ')))\n")
    file_for_running.write("\tcount -= 1\n")
    file_for_running.write("print '%s' % str(sum(variable)+reduce(lambda x,y: x*y, variable))+'/%s' % str(reduce(lambda x,y: x*y, variable))")

file_for_running = open("run_me.py", "w")
count = create_string()[0]
generate_of_run_file(count)
file_for_running.close()
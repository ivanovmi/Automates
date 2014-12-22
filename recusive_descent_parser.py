import pyparsing


def create_string():
    variable_of_function = pyparsing.Word(pyparsing.alphas)
    number = pyparsing.Word(pyparsing.nums)

    pars_string = pyparsing.Literal("(") + number + pyparsing.Literal("*") + variable_of_function + \
                  pyparsing.Literal("+") + number + pyparsing.Literal(")") + pyparsing.Literal("/") + \
                  pyparsing.Literal("(") + number + pyparsing.Literal("*") + variable_of_function + \
                  pyparsing.Literal("+") + number + pyparsing.Literal(")")

    input_file=open("input", "r")
    input_function=input_file.readline()
    # input_function=raw_input("Enter the input_function: ")
    # input_function = "(5*x+43)/(4*x+9)"
    input_file.close()
    return pars_string.parseString(input_function)


def generate_of_run_file():
    file_for_runinning.write("from __future__ import division\n")
    file_for_runinning.write("variable = int(raw_input('Enter the value of variable: '))\n")
    file_for_runinning.write("a1 = %s\n" % create_string()[1])
    file_for_runinning.write("a2 = %s\n" % create_string()[5])
    file_for_runinning.write("b1 = %s\n" % create_string()[9])
    file_for_runinning.write("b2 = %s\n" % create_string()[13])
    file_for_runinning.write("print (a1*variable+a2)/(b1*variable+b2)")


file_for_runinning = open("run_me.py", "w")
generate_of_run_file()
file_for_runinning.close()

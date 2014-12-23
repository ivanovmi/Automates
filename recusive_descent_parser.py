import pyparsing


def create_string():
    name_of_array = pyparsing.Word(pyparsing.alphas)
    number = pyparsing.Word(pyparsing.nums)
    input_file = open("input", "r")
    input_data = input_file.readline()
    input_file.close()
    parse_input = []
    arrays=[]
    address = input_data.split(";")
    for i in address:
        pars_string = name_of_array + pyparsing.Literal("[") + number + pyparsing.Literal("]") + \
                      pyparsing.Literal("[") + number + pyparsing.Literal("]")
        parse_input.append(pars_string.parseString(i))
    for i in parse_input:
        if i[0] not in arrays:
            arrays.append(i[0])
    generate_of_run_file(address,arrays)


def generate_of_run_file(array,arrays):
    file_for_runnining.write("from random import randint\n")
    for i in arrays:
        file_for_runnining.write("%s = [[0]*10]*10\n" % i)
    for i in array:
        file_for_runnining.write("%s = randint(0,100)\n" % i)
    for i in arrays:
        file_for_runnining.write("print %s\n" % i)


file_for_runnining = open("run_me.py", "w")
create_string()
file_for_runnining.close()

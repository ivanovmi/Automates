import pyparsing

f = open("pars.txt", 'r')
count = int(f.readline())

variable = pyparsing.Word(pyparsing.alphas + pyparsing.nums)
fraction = pyparsing.nums[1] + pyparsing.Literal("/") + variable
pars_String = pyparsing.nums[1]
ex = pyparsing.Word(pyparsing.alphas + pyparsing.alphanums)
num = pyparsing.nums
while count != 0:
    pars = pyparsing.Literal("(") + num + pyparsing.Literal("*") + ex + pyparsing.Literal("+") + \
           num +pyparsing.Literal(")") + pyparsing.Literal("/") + pyparsing.Literal("(") + num + \
           pyparsing.Literal("*") + ex + pyparsing.Literal("+") + num +pyparsing.Literal(")")
    count -= 1

function=raw_input("Enter the function: ")

print pars_String.parseString(function)

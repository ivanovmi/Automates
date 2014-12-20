import pyparsing

ex = pyparsing.Word(pyparsing.alphas)
num = pyparsing.nums

pars_String = pyparsing.Literal("(") + num + pyparsing.Literal("*") + ex + pyparsing.Literal("+") + \
                num +pyparsing.Literal(")") + pyparsing.Literal("/") + pyparsing.Literal("(") + num + \
                pyparsing.Literal("*") + ex + pyparsing.Literal("+") + num +pyparsing.Literal(")")


#function=raw_input("Enter the function: ")
function="(5*x+4)/(4*x+5)"
print pars_String.parseString(function)


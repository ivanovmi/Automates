import pyparsing

f = open("pars.txt", 'r')
count = int(f.readline())

variable = pyparsing.Word(pyparsing.alphas + pyparsing.nums)
fraction = pyparsing.nums[1] + pyparsing.Literal("/") + variable
pars_String = pyparsing.nums[1]
while count != 0:
    pars_String = pars_String + pyparsing.Literal("+") + fraction
    count -= 1

test = "1+1/x1+1/x2+1/x4"

print pars_String.parseString(test)

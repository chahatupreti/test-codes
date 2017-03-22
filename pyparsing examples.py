from pyparsing import *

# lambda to define expressions
def makeExpr(ch):
#    print (34)
    print (ch)
    expr = Literal(ch).setResultsName(ch, listAllMatches=True)
#    print type(ch)
    print (expr)
    return expr

expr = OneOrMore(MatchFirst(makeExpr(c) for c in "abc"))
expr.setParseAction(lambda tokens: [[a,len(b)] for a,b in tokens.items()])


tests = """\
abc
bbbc
cccaa
""".splitlines()

#for t in tests:
#    print (t,expr.parseString(t).asList())
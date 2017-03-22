# -*- coding: utf-8 -*-
"""
Created on Sat Mar 11 19:19:34 2017
@author: Krishna
"""

from pyparsing import *
import re

UPTO, AND, OR, WORDS = map(Literal, "upto AND OR words".split())
keyword = UPTO | WORDS | AND | OR
LBRACE,RBRACE = map(Suppress, "{}")
integer = pyparsing_common.integer()

LINE_CONTAINS, LINE_STARTSWITH, LINE_ENDSWITH = map(Literal,
    """LINE_CONTAINS LINE_STARTSWITH LINE_ENDSWITH""".split()) # put option for LINE_ENDSWITH. Users may use, I don't presently

#NOT, AND, OR = map(Literal, "NOT AND OR".split())
BEFORE, AFTER, JOIN = map(Literal, "BEFORE AFTER JOIN".split())


word = ~keyword + Word(alphas)
phrase = Group(OneOrMore(word))
upto_expr = Group(LBRACE + UPTO + integer("numberofwords") + WORDS + RBRACE)
join_expr = Group(word + JOIN + word)

class Node(object):
    def __init__(self, tokens):
        self.tokens = tokens

    def generate(self):
        pass


class LiteralNode(Node):
    def generate(self):
        return "(%s)" %(' '.join(self.tokens[0])) # here, do something to merge the elements, so that re.escape does not have to do an escape for the entire list
    def __repr__(self):
        return repr(self.tokens[0])


class AndNode(Node):
    def generate(self):
        tokens = self.tokens[0]
        return '.*'.join(t.generate() for t in tokens[::2]) # change this to the correct form of AND in regex

    def __repr__(self):
        return ' AND '.join(repr(t) for t in self.tokens[0].asList()[::2])


class OrNode(Node):
    def generate(self):
        tokens = self.tokens[0]
        return '|'.join(t.generate() for t in tokens[::2])
    def __repr__(self):
        return ' OR '.join(repr(t) for t in self.tokens[0].asList()[::2])


class UpToNode(Node):
    def generate(self):
        tokens = self.tokens[0]
        ret = tokens[0].generate()
        print (123123)
        word_re = r"\s+\S+"
        space_re = r"\s+"
        for op, operand in zip(tokens[1::2], tokens[2::2]):
            # op contains the parsed "upto" expression
            ret += "((%s){0,%d}%s)" % (word_re, op.numberofwords, space_re) + operand.generate()
        print ret
        return ret


    def __repr__(self):
        tokens = self.tokens[0]
        ret = repr(tokens[0])
        for op, operand in zip(tokens[1::2], tokens[2::2]):
            # op contains the parsed "upto" expression
            ret += " {0-%d WORDS} " % (op.numberofwords) + repr(operand)
        return ret

class JoinNode(Node):
    def generate(self):
        tokens = self.tokens[0]
        print (tokens, 17)
        ret = tokens[0].generate()
#        word_re = r"\s+\S+"
#        space_re = r"\s+"
#        for op, operand in zip(tokens[1::2], tokens[2::2]):
#            # op contains the parsed "upto" expression
#            ret += "((%s){0,%d}%s)" % (word_re, op.numberofwords, space_re) + operand.generate()
#        return ret


    def __repr__(self):
        print (2342314123412341234)
        return "20"
#        tokens = self.tokens[0]
#        ret = repr(tokens[0])
#        for op, operand in zip(tokens[1::2], tokens[2::2]):
#            # op contains the parsed "upto" expression
#            ret += " {0-%d WORDS} " % (op.numberofwords) + repr(operand)
#        return ret

#IMPLICIT_AND = Empty().setParseAction(replaceWith("AND"))

phrase_expr = infixNotation(phrase.setParseAction(LiteralNode),
        [
        (upto_expr, 2, opAssoc.LEFT, UpToNode),
        (join_expr, 2, opAssoc.LEFT, JoinNode),
        (AND, 2, opAssoc.LEFT, AndNode),
        (OR, 2, opAssoc.LEFT, OrNode),
        ])


tests = """\
        xyz
        xyz dsf JOIN wer asd OR abc sdfas
        xyz there are {upto 3 words} def then {upto 4 words} here
        xyz abc there {upto 4 words} def""".splitlines()

tests1 = """
LINECONTAINS overexpressing gene
""".splitlines()
        
for t in tests:
    t = t.strip()
    if not t:
        continue
#    print(t, 12)
    try:
        parsed = phrase_expr.parseString(t)
    except ParseException as pe:
        print(' '*pe.loc + '^')
        print(pe)
        continue
#    print(parsed, 13)
    print (parsed[0], 14)
#    print (type(parsed[0]))
#    print parsed.dump()
    print
    print(parsed[0].generate(), 15)
    print
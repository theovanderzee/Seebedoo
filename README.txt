Seebedoo
========

Seebedoo
Test




https://github.com/emilmont/pyStatParser

up vote
7
down vote
You can take a look at pyStatParser, a simple python statistical parser that returns NLTK parse Trees. It comes with public treebanks and it generates the grammar model only the first time you instantiate a Parser object (in about 8 seconds). It uses a CKY algorithm and it parses average length sentences (like the one below) in under a second.

>>> from stat_parser import Parser
>>> parser = Parser()
>>> print parser.parse("How can the net amount of entropy of the universe be massively decreased?")
(SBARQ
  (WHADVP (WRB how))
  (SQ
    (MD can)
    (NP
      (NP (DT the) (JJ net) (NN amount))
      (PP
        (IN of)
        (NP
          (NP (NNS entropy))
          (PP (IN of) (NP (DT the) (NN universe))))))
    (VP (VB be) (ADJP (RB massively) (VBN decreased))))
  (. ?))
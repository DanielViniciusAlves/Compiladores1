# Grammatical Predictive Analyzer

## This directory has the purpose of defining a Grammatical Predictive Analyzer and implementing the code in Python and C for the following context free grammar:



<center>

![alt text](../assets/top_down_context_free_grammar.png "Context Free Grammar")

</center>

## Defining a Grammatical Predictive Analyzer

A Grammatical Predictive Analyzer is basically a program that will begin at the root and go to the leafs of the semantic grammar that was created. At the beginning the first *token* will be defined as the lookahead, if the *token* is recognized the next *token* will become the new lookahead.

* The Analyzer will be a recursive function.
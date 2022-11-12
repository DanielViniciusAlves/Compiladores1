# Defining a Free Context Grammar: class from the day 11/09/2022

## What is the purpose of a free context grammar?

A free context grammar is used to specify a language, this can be done because the grammar will be able to define a series of ways that the language work.

## Infixed Notation:

Lets consider the operation: 1+2x3. There are three different ways that this operation can be rearranged, infixed, postfixed and prefixed:
    
    Infixed: 1+2x3;
    Prefixed: +1x23;
    Postfixed: 23x1+.
    
* The only one that demand the utilization of parenthesis is the infixed type of notation, this can be demonstrated as the operation itself is made:

    1+2x3 -> 1+(2x3) -> 1+6 -> (1+6) -> 7;

This means that the infixed notation itself will generate a ambiguity, to solve this problem is used a associative analyses(in this case to the left) and a analyses of the precedence of the operator.

## Elements from a Free Context Grammar

* Terminal: is characters that in a group have a meaning and cannot be expanded(cannot be changed into **anything**). It is going to be in the right of the non-terminal.

* Departure Symbol: is the first production from the grammar.

* Non-terminal: is the elements in italic, always will appear on the most left and can be defined as the elements which can be expanded.

* Tokens: a character or a group of characters that have a meaning.

## How to read a Grammatical Tree?

The grammatical tree is read from the most left to the right, going to the leaf at first.

* Leaf: it will contain the token or the E(empty symbol).
* Root: it will contain the departure state.
* Interior Node: it will contain the non terminals.

By its definition a leaf cannot be expanded!

When a grammar is ambiguous will be possible to generate a series of different trees, but all of them will have the same production.

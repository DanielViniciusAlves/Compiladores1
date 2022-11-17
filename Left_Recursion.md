# Left Recursion : class from the day 16/11/2022

## Defining first symbol:

First symbol is a pack of *tokens* that initialize some grammar. For example, considering the grammar:

```
S -> aA|aB|b
A -> S|c
B -> bA|aB|e
```

* Considering *e* as an empty chain.

The first symbol of the aA will be "a", and so on.

## Predictive Parser.

The importance of defining the first symbol is to determinate if is possible to do a predictive parser to some grammar. This can be done because the definition of the first symbol can say, when there is a intersection between first symbol, if is predictive or not the parser that can be maid. So if we consider the following grammar:

```
S -> aA|aB|b
A -> S|c
B -> bA|aB|e
```

There is a intersection in the production of the start symbol (aA and aB). Because of this intersection we cant do a predictive parser to this grammar.

The advantage of this type of translation is that facilitate the implementation of operations with a stack.

* A important idea to have while making a predictive parser is that at the end of the analyzes if there is still tokens to be analyzed the chain that was given is invalid.

## Left Recursion

### Defining Left Recursion:

A grammar will be left recursive when the non-terminal is the first symbol of the production. For example:

```
expr -> expr + digit | expr - digit | digit
```

In the example grammar we can see that the first symbol will be *expr* and *digit*. The expr is a non-terminal symbol so the grammar is left recursive.

* We cant use a predictive top-down parser in a grammar that is left recursive.

## Right Recursion

### Defining Right Recursion:

A grammar will be left recursive when the non-terminal is the last symbol of the production. For example:

```
expr -> digit + expr | digit - expr | digit
```

In a grammar right recursive is possible to use a predictive top-down parser, but the disadvantage is that the association will be at right. This is bad because in a expression that exist operators that are right associative the translation with the right recursive grammar will be harder.
So is best to remove the left recursion without loosing the left association. For example:

```
A -> Aa | Ab | c
```

We can see that every production will have to end with "c". So we can make the following action:

```
A -> cR 
R -> aR | bR | e
```

Another example:

```
X -> Xx | y | Xz | wX
```

We can see that every production will have to end with "y" or w. So we can make the following action:

```
X -> yR | wXR
R -> zR | xR | e
```

With this steps, with a left recursive grammar, we will make it become right recursive maintaining the left associativity. And using the idea defined before: "This can be done because the definition of the first symbol can say, when there is a intersection between first symbol, if is predictive or not the parser that can be maid.", we can say that is possible to make a predictive top-down parser.


* The R will always end with a empty chain (*e*).


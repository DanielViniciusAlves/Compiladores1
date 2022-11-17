# Defining Compiler: class from the day 11/02/2022

## What is a compiler?

Compiler is a program that has the objective to read the source language and then translate to the target language. A compiler can also translate to the same language, this happen in a indentor for example, but he most common use is from a high level language to a low level such as Assembly.

## Defining each part faze from the compilation:

1. Lexical Analyzer: the characters form the target program is read, from left to right, and then will group each token.

2. Syntactic Analyzer: this type of analysis will have the objective to generate a grammatical tree, the tree will have the purpose to organize the tokens hierarchically.   

3. Sematic Analyses: will have the purpose to analyses semantic errors in the target program and type errors. An example of this is a operation of adding between a float and a integer.

4. Intermediary Code Generator: in this faze the compiler will transform the grammatical tree in a intermediary code, this code will be interpreted by a abstract machine.

5. Code Optimize: this is the faze responsible to optimize the intermediary code, with the objective to improve the performance of the Assembly code to the target program.

6. Code Generator: this is the last part from the compilation, will produce a target code, form the most part in Assembly.

* Token: is a character or a sequence of characters with a meaning, such as an *if* in the C language for example.

## Dividing the compilation:

* The Compilation can be divided in two different ways:

    1. Analyses and synthesis: analyses will be composed the lexical analyses, syntactic analyses and semantic analyses. The final product from the analyses faze will be a syntactic tree with possibly some changes from the semantic analyses. Now the synthesis faze will be composed by the intermediary code generator, optimize and finally the code generator, with the final product as the target program.

    2. Frontend and Backend(Vanguarda e Retaguarda): the frontend will be composed by lexical analyses, syntactic analyses, semantic analyses and intermediary code generator, so the final product will be the intermediary code that can also be defined as source code. The backend will be composed by two fazes the optimizer and the code generator, therefore the product of this faze is the target program.

* The frontend is focused in the target language and the backend is focused in the target machine.

* The intermediary code that is generated can be defined as one code to a abstract machine.
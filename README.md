
# ☀️ Analyzer syntactic for operator grammar
Analyzer syntactic for operator grammar in Python.

## 💻 Requirements

Python3 and pip3.

(opcional) If you want, you can create a virtual environment:

```shell
python3 -m venv env
```

Activate virtual environment:

- Unix/macOS

```shell
source env/bin/activate
```

- Windows

```shell
./env\Script\activate
```

### Install requirements:

```shell
pip3 install -r requirements.txt
```

For install coverage

## 🔥 For run it

```shell
python3 main.py
```

## 💡 How to use it

1) `RULE <no-terminal> [<symbol>]`

Define a new rule in the grammar for the <no-terminal> symbol. The list of symbols in
`[<symbol>]` is a space-separated (potentially empty) list of terminal symbols or
not terminals.

For example:

RULE A a A b - Represents the rule: A → a A b

RULE B - Represents the rule: B → λ

The program should report an error and ignore the action if the symbol placed on the left side
of the rule is not non-terminal or if the expressed rule does not correspond to a grammar of operators.


2) `INIT <no-terminal>`

Sets the initial symbol of the grammar to be the symbol in <no-terminal>.
For example: INIT B - Sets the symbol B as the initial symbol of the grammar.
The program should report an error and ignore the action if the symbol is not non-terminal.


3) `PREC <terminal> <op> <terminal>`

Establishes the relationship between two terminals (or $). This `<op>` operation can be:

`<` when the first terminal has lower precedence than the second

`>` when the first terminal has higher precedence than the second

`=` when the first terminal has the same precedence as the second

For example:

PREC + < * - Sets that + has lower precedence than *

PREC (=) - Sets that (has the same precedence as)

PREC $ > n - Sets that $ (border marker) has higher precedence than n

The program should report an error and ignore the action if the symbols involved are not symbols
terminals or if the operator in `<op>` is invalid.


4) `BUILD`

Build a parser with the information provided so far.
Must report calculated values for functions f and g (views in class) or report what to build
such functions is impossible, showing evidence for it.


5) `PARSE <string>`

It performs the parsing process on the string supplied in <string>. Must show
each of the steps, including:

Stack - Current status of the stack

Input - Current status of the input. This statement should clearly show the relationships of
precedents and the point where it is currently being read (see example).

Action - Action taken (read or reduce by a particular rule)

For example:

PARSE n + n * n - Perform the process on the string n + n * n

The program should report an error and ignore the action if the symbols involved are not symbols
terminals, there are non-comparable symbols or if you have not BUILD previously. Between each to
symbol terminals in `<string>` there can be any (potentially zero) amount of
Blanks.


6) `EXIT`

You must exit the simulator.

## 🔍 For run the tests

```shell
coverage3 run --source=memory_manager -m unittest test.py
```

#### Coverage of the tests

```shell
coverage3 report -m
```

| Module | Coverage |
|:----:|:--:|
| Analyzer | % |
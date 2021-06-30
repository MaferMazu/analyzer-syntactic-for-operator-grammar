from sys import exit, argv
from analyzer import Analyzer


def main():
    """
    Main
    """
    print("*" * 30)
    print("""Welcome to this analyzer syntactic :D Happy coding\n""")
    analyzer = Analyzer()
    while True:
        my_input = input(">> ")
        elems = my_input.split(" ")
        command = elems[0]
        rest = []
        if len(elems) > 1:
            rest = elems[1:]
        if command == "EXIT":
            exit(0)
        elif command == "PREC" and len(rest) == 3:
            analyzer.add_precedence(rest)

        elif command == "RULE" and len(elems) > 1:
            analyzer.add_rule(rest)

        elif command == "BUILD":
            analyzer.build()

        elif command == "PARSE":
            analyzer.parse(rest)

        elif command == "INIT" and len(elems) > 1:
            analyzer.set_init(elems[1])

        else:
            print_help()


def print_help():
    """ Print help for user """

    response = """RULE <no-terminal> [<symbol>]
For example:
RULE A a A b - Represents the rule: A → a A b

INIT <no-terminal>

PREC <terminal> <op> <terminal>
Establishes the relationship between two terminals (or $). This <op> operation can be:
< when the first terminal has lower precedence than the second
> when the first terminal has higher precedence than the second
= when the first terminal has the same precedence as the second
For example:
PREC + < * - Sets that + has lower precedence than *

BUILD

PARSE <string>

EXIT\n"""

    print(response)


if __name__ == "__main__":
    main()

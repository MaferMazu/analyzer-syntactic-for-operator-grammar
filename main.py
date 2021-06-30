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

        elif command == "PARSER":
            pass

        elif command == "INIT" and len(elems) > 1:
            analyzer.set_init(elems[1])

        else:
            print_help()


def print_help():
    """ Print help for user """

    response = """RESERVAR <nombre> <cantidad>
        Representa una reserva de espacio de <cantidad> bloques,
        asociados al identificador <nombre>.
        LIBERAR <nombre>
        Representa una liberación del espacio que contiene el
        identificador <nombre>.

        MOSTRAR
        Debe mostrar una representación gráfica (en texto) de las
        listas de bloques libres, así como la información de nombres
        y la memoria que tienen asociada a los mismos.

        SALIR
        Debe salir del simulador.\n"""

    print(response)


if __name__ == "__main__":
    main()

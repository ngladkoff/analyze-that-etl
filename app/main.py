from user_interaction.input_numbers import ask_integer
from etl.etl_factory import EtlFactory

SALIR = 0


def main():
    option = 1
    while option != 0:
        option = ask_integer("Ingrese opción [1-Scrum | 2-Psico | 0-Salir]: ",
                             0,
                             2,
                             "Ingrese un número mayor a 0",
                             "Ingrese un número menor a 2")
        if option == SALIR:
            print("Adios")
            return 0

        etl = EtlFactory.create_etl('scrum' if option == 1
                                    else 'psico', True, True)
        etl.start()


if __name__ == '__main__':
    main()

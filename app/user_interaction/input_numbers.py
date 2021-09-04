
def ask_integer(message, valmin, valmax, min_err_msg, max_err_msg) -> int:
    while True:
        try:
            val = int(input(message))
            if val < valmin:
                print(min_err_msg)
            elif val > valmax:
                print(max_err_msg)
            else:
                return val
        except ValueError:
            print("Debe ingresar un número válido")

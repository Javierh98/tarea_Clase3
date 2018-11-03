# =========================== Funciones =========================== #
def test_sumar(p_num_1, p_num_2):
    return p_num_1 + p_num_2


def test_restar(p_num_1, p_num_2):
    return p_num_1 - p_num_2


def test_multiplicar(p_num_1, p_num_2):
    return p_num_1 * p_num_2


def test_dividir(p_num_1, p_num_2):
    try:
        return p_num_1 / p_num_2
    except ZeroDivisionError:
        print("No se puede dividir entre 0")
        return "Imposible de ejecutar"

# =========================== Input de datos =========================== #
while True:
    print("================= Calculadora en Python 3 =================")
    try:
        opcion_1 = (int(input("Introdusca el primer numero: ")))
        opcion_2 = (int(input("Introdusca el primer numero: ")))
        break

    except ValueError:
        print("Valores incorrectos")

operacion = (input("Introdusca el tipo de operacion (suma, resta, multiplicacion, divide): ").lower())

# =========================== Condicionales de las operaciones =========================== #
if operacion == "suma":
    print(test_sumar(opcion_1, opcion_2))

elif operacion == "resta":
    print(test_restar(opcion_1, opcion_2))

elif operacion == "multiplicacion":
    print(test_multiplicar(opcion_1, opcion_2))

elif operacion == "divide":
    print(test_dividir(opcion_1, opcion_2))

else:
    print("Error en la ejecucion")

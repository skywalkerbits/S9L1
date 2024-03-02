
def dividir(a, b):
    if b == 0:
        return "No se puede dividir por cero"
    else:
        return a / b


if __name__ == "__main__":
    print("División:", dividir(5, 3))
    print("Intento de dividir por cero:", dividir(5, 0))

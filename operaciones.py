# fichero operaciones.py . Donde se guardan todas las operaciones que ejecuta nuestra app/calculadora

# suma
def sumar(self):
        self.assertEqual(sumar(3, 2), 5)
        self.assertEqual(sumar(-1, 1), 0)
        self.assertEqual(sumar(-1, -1), -2)

#resta
def restar(a, b):
    return a - b

# division
def dividir(a, b):
    if b == 0:
        return "No se puede dividir por cero"
    else:
        return a / b

# multiplicacion    
def multiplicar(a, b):
    return a * b

    


if __name__ == "__main__":
 # para la suma
    print(sumar(5, 3))
 # para la division
    print("División:", dividir(5, 3))
 # intento de dividir por 0
    print("Intento de dividir por cero:", dividir(5, 0))
 # para la multiplicacion
    print("Multiplicación:", multiplicar(5, 3))
 # para la resta
    print("Resta:", restar(5, 3))
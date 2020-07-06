# Los operadores son signos, símbolos o palabras que el interprete utiliza
# para hacer una operación específica

# OPERADORES MATEMÁTICOS
"""
+ Operador de Suma
- Operador de Resta
- Operador de Negativo
* Operador de Multiplicación
** Operador de Exponente
/ Operador de división
// Operador de división entera
% Operador de Módulo o Resto
"""

# Reglas de precedencia de las operaciones matemáticas
"""
En orden de precedencia
1. Parentesis
2. Exponente
3. Multiplicación
4. División
5. Suma
6. Resta
"""

numero1 = 10
numero2 = 5

# Realizar todas las operaciones aritmeticas utilizando estos dos números
print("Suma")
print(numero1 + numero2)
print("Resta")
print(numero1 - numero2)
print("Multiplicación")
print(numero1 * numero2)
print("Exponente")
print(numero1 ** numero2)
print("División")
print(numero1 / numero2)
print("División entera")
print(numero1 // numero2)
print("Módulo / Resto")
print(numero1 % numero2)

resultado = 12 * 5 + 2 / 3 ** 2
print(resultado)

resultado1 = (12 * 5) + (2 / (3 ** 2))
print(resultado1)

resultado2 = (12 * 5) + (2 / 3) ** 2
print(resultado2)

# OPERADORES PARA CADENAS
"""
+ Operador de Concatenación
* Operador de Repetición
"""

cadena1 = "Hola "
cadena2 = "Mundo"

cadenas_unidas = cadena1 + cadena2
print(cadenas_unidas)

cadenas_repetidas = cadena1 * 3
print(cadenas_repetidas)

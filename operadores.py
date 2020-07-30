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

# OPERADORES DE RELACIÓN
# Los operadores de relación evaluan si 2 valores u objetos cumplen con una
# condición.
# El resultado de dicha evaluación es un objeto booleano (bool)

"""
== Igual A?
!= Distinto de?
> Mayor que?
< Menor que?
>= Mayor o Igual que?
<= Menor o Igual que?
"""

numero1 = 10
numero2 = 5
numero3 = 10.0
numero4 = -10
numero5 = 5
numero_cadena = "10"

print("Operadores")
print("")

igual = numero1 == numero2
print(igual)
igual = numero2 == numero5
print(igual)
igual = numero2 == numero3
print(igual)
igual = numero1 == numero_cadena
print(igual)

# distinto
distinto = numero1 != numero2
print(distinto)
distinto = numero2 != numero5
print(distinto)
distinto = numero2 != numero3
print(distinto)
distinto = numero1 != numero_cadena
print(distinto)

mayor_que = numero1 > numero3
print(mayor_que)
mayor_que = numero1 > numero2
print(mayor_que)

menor_que = numero1 < numero3
print(menor_que)
menor_que = numero1 < numero2
print(menor_que)
menor_que = numero1 < int(numero_cadena)
# conversión entero ya que < solo compara por valor dentro del mismo tipo de
# dato
print(menor_que)

mayor_igual = numero1 >= numero2
print(mayor_igual)
mayor_igual = numero2 >= numero5
print(mayor_igual)
mayor_igual = numero1 >= numero3
print(mayor_igual)

menor_igual = numero1 <= numero2
print(menor_igual)
menor_igual = numero2 <= numero5
print(menor_igual)
menor_igual = numero1 <= numero3
print(menor_igual)

#Algoritmo para calificar ejercicios

taller_1 = 0.20
taller_2 = 0.15
cuestionario_1 = 0.220
cuestionario_2 = 0.1
proyecto_final = 0.33

taller1 = float (input("Ingresa la nota del taller # 1: "))
taller2 = float (input("Ingresa la nota del taller # 2: "))
cuestionario1 = float (input("Ingresa la nota del cuestionario # 1: "))
cuestionario2 = float (input("Ingresa la nota del cuestionario # 2: "))
proyectofinal = float (input("Ingresa la nota del proyecto final: "))

nota_final = (taller1 *taller_1) + (taller2 * taller_2) + (cuestionario1 * cuestionario_1) + (cuestionario2 * cuestionario_2) + (proyecto_final * proyectofinal)
print (f"Tu nota final es de ", nota_final)
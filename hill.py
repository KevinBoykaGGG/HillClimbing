import random 
import string 

# ESTA FUNCION ES OPCIONAL, LA USAMOS PARA GENERAR ESTADO SINICIALES ALEATORIOS
def generate_random_solution():
	length=5 
	return [random.choice(string.printable) for _ in range(length)]


# ESTA FUNCION COMPARA LA SOLUCION ACTUAL CON LA SOLUCION OBJETIVO
def evaluate(solution):
	# ESTABLECEMOS SOLUCION OBJETIVO
	target = list("12345")
	# INICIALIZAMOS EN 0 LA DIFERENCIA ENTRE LA SOLUCION ACTUAL Y EL OBJETIVO
	diff = 0
	# PARA CADA UNA DE LAS LETRAS DE AMBOS STRINGS VAMOS A OBTENER EL VALOR UNICODE DE LAS LETRAS QUE SE ENCUENTRAN EN LA MISMA POSICION
	for i in range(len(target)): 
		s = solution[i] 
		t = target[i] 
		# ALMACENAMOS EL VALOR ABSOLUTO DE LA DIFERENCIA, EN CASO DE QUE FUERAN LA MISMA LETRA LA DIFERENCIA SERIA DE 0
		diff += abs(ord(s) - ord(t))
	# REGRESAMOS LA SUMATORIA DE LAS DIFERENCIA DE CADA CARACTER DE LA SOLUCION ACTUAL CONTRA LA SOLUCION OBJETIVO
	return diff


# ESTA FUNCION LO QUE HACE ES MODIFICAR CARACTER A CARACTER EL STRING ACTUAL PARA PROPONER UN ESTADO DIFERENTE
def mutate_solution(solution):
	index = random.randint(0, len(solution) - 1) 
	# solution[index] = random.choice(string.printable) 
	solution[index] = str(random.randint(1, len(solution)))


# ESTABLECEMOS LA CADENA DE INICIO
#best = generate_random_solution()
best = "54321";
best_score = evaluate(best) 


# REALIZAMSO LA SIGUIENTE ITERACION HASTA TENER UN "best_score" CON VALOR DE 0
while True:
	print('Best score so far', best_score, 'Solution', "".join(best)) 
	 
	 # CUANDO EL SCORE ACTUAL SEA IGUAL A CERO DETENEMOS EL CICLO PUES HEMOS LLEGADO AL ESTADO META
	if best_score == 0: 
		break
	 
	 # AQUI MANDAMOS A LLAMAR A "mutate_solution" QUE ES LA QUE PROPONE UNA CADENA DIFERENTE A LA ACTUAL PARA SER EVALUADA
	new_solution = list(best)
	mutate_solution(new_solution) 
	
	# SLA SOLUCION ACTUAL ES EVALUADA PARA OBTENER EL "score" ESTE DATO NOS IDICA UN NUMERO ENTERO QUE EN CASO DE NO HABER DIFERENCIA CON EL VALOR OBJETIVO
	# DEVOLVERA UN 0
	score = evaluate(new_solution)

	# SI OBTENEMOS UN MEJOR SCORE CON ESTA SOLUCION PROPUESTA INTERCAMBIAMOS LA MEJOS SOLUCION (best) POR LA NUEVA SOLUCION PROPUESTA (new_solution)
	if evaluate(new_solution) < best_score:
		best = new_solution
		# ACTUALIZAMSO EL MEJOR "score" OBTENIDO HASTA EL MOMENTO
		best_score = score
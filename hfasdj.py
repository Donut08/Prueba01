def preguntar(pregunta, respuestas):

    for i in range(len(respuestas)):
        respuestas[i] = respuestas[i].lower()
    
    while True:
        p = input(f"{pregunta} {respuestas}: ").lower()

        for r in respuestas:
            if p == r:
                print("OK")
                return p
        
        print("Esa no es una opción\n")

respuesta = preguntar("te gusta la comida?: ", ["Si", "nO"])
print(f"Respuesta: {respuesta}")
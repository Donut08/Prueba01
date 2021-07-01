def question(question, answers):

    for i in range(len(answers)):
        answers[i] = answers[i].lower()
    
    while True:
        p = input(f"{question} {answers}: ").lower()

        for r in answers:
            if p == r:
                print("OK")
                return p
        
        print("Esa no es una opción\n")

answer = question("te gusta la comida?: ", ["Si", "nO"])
print(f"Respuesta: {answer}")
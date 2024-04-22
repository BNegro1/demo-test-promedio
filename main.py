l_notasPorc = [] # Lista que sera tuplas (notas, promedio)
promedio = 0
cantNotas = int(input("Ingrese cantidad de notas: "))
for x in range(cantNotas):
    notx = float(input(f'Ingrese nota {x+1}: '))
    if notx >= 1.0:   
        porcentajex = int(input("Ingrese un porcentaje: "))
        if porcentajex > 0:
            l_notasPorc.append((notx, porcentajex))
        else:
            print("Ingrese un porcentaje válido.")
            break
    else:
        print("Ingrese una nota mayor a 1.0.")
        break
print(l_notasPorc)
for nota, porcentaje in l_notasPorc:
    promedio += nota * (porcentaje / 100)
print(f'Promedio: {round(promedio)}')
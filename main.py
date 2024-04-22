l_notas = []
l_por = []
l_notasPorc = []
promedio = 0
cantNotas = int(input("Ingrese cantidad de notas: "))
for x in range(cantNotas):
    notx = float(input(f'Ingrese nota {x+1}: '))
    if notx >= 1.0:   
        porcentajex = int(input("Ingrese un porcentaje: "))
        if porcentajex > 0:
            l_notasPorc.append(notx)
            l_notasPorc.append(porcentajex)
            l_notas.apped(notx)
            l_por.append(porcentajex)
        else:
            print("Ingrese un porcentaje válido.")
            break
    else:
        print("Ingrese una nota mayor a 1.0.")
        break
print(l_notasPorc)
for x in l_notasPorc:
    promedio += ()
print(promedio)
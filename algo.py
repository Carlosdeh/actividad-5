enemigos = []
seguir = True
while seguir:
    nomenem = str(input())
    if nomenem == "FIN":
        break
    enemigos.append(nomenem)
    

posicion = int(input())
atcenem = enemigos[posicion]

print(f"{atcenem} fue atacado!")
print(len(enemigos)-1)


for i in enemigos:
    if i != atcenem:
        print(i)



pridos = enemigos[:2] 
ultdos = enemigos[-2:]

print(pridos+ultdos)
resultado = [ 
    ["Figo", "João", "Marta"],   
    ["Figo", "João", "Marta"],   
    ["Marta", "João", "Figo"] 
]

 
resultado_figo = 0
resultado_joao = 0
resultado_marta = 0
 
for x in resultado:
    if "Figo" == x [0]:
        resultado_figo += 1
 
    elif "João" == x [0]:
        resultado_joao += 1
 
    else:
        resultado_marta += 1


lista_resultados = [resultado_figo, resultado_joao, resultado_marta]

if resultado_marta == resultado_figo == resultado_joao:
    print("It's a tie")
elif max(lista_resultados) == resultado_figo :
    print("Figo Wins!")
elif max(lista_resultados) == resultado_joao :
    print("João Wins!")
else:
    print("Marta Wins")

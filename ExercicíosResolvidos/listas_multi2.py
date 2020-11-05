lista = [[10],[1,2,3], [5,6], [0,2,3]]
 
multi = []

for x in lista:
    previous_value = 1
    for y in x:
        previous_value = y * previous_value
    multi.append(previous_value)

print (multi)

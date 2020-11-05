l = [7,4,1,7,2,3,5,1]

temp_l = []

for element in l:
    if element not in temp_l:
        temp_l.append(element)

l = temp_l

print("List with no duplicates", l)


#OU

l = [7,4,1,7,2,3,5,1]
l = list(dict.fromkeys(l))

print("List with no duplicates v2", l)
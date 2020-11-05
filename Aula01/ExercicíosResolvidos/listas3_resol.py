
l = [7,4,1,7,2,3,5,1]

temp_l = []

for element in l:
    if element not in temp_l and element % 2 != 0:
        temp_l.append(element)

l = temp_l
l.sort(reverse=False)

print("List with no duplicates, sorted and with no evens: \n",l)


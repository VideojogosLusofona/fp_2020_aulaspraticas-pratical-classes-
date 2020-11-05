def wabbbajack(stuff):

    if isinstance(stuff, int) or isinstance(stuff,float):
        return str(stuff)
    elif isinstance(stuff, str) :
        return len(stuff)
    else:
        return "Sorry, that’s not a float or string"


print(wabbbajack(1.2))
print(isinstance(wabbbajack(1.2), str))
print(wabbbajack(5))
print(isinstance(wabbbajack(5), str))
print(wabbbajack("HAHAHAHAHADJhajwdhabjdbajn")) 
print(wabbbajack([1,2]))


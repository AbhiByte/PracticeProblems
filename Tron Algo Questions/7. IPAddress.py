#Q7. IP validator done. 
ef ip(input):
    arr = input.split(".")
    if len(arr) != 4:
        return "Not IP"
    elif len(arr) == 4:
        for x in arr:
            if x.isnumeric() == True:
                if int(x) > 255 or int(x) < 0:
                    return "Not IP"
            if x.isnumeric() == False:
                return "Not IP"
        return "IP"

print(ip("a.134.21.3.4"))

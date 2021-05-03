# 7. Reverse Integer
def reverseInt(x):
    x = str(x)
    if x[-1] != "0" and x[0] != "-":
        x = x[::-1]
    elif x[-1] == "0" and x[0] != '-':
        x = x[::-1]
    elif x[-1] == "0" and x[0] == "-":
        x = x[1::]
        x = x[::-1]
        x = x[1::]
        x = "-" + x
    elif x[0] == "-":
        x = x[1:]
        x = x[::-1]
        x = "-" + x
    x = int(x)
    if x > 2**31 - 1 or x < -1 * (2**31):
        x = 0
    return x


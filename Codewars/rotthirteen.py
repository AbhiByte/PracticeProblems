def rot13(message):

    inp = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    output = 'NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm'

    for element in message:
        if element.isalpha() == True:
            message.replace(element, output[inp.find(element)])
    return message

print(rot13("EBG13 rknzcyr."))

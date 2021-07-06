def rot13(message):

    inp = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    output = 'NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm'

    mess_lst = list(message)
    for i, item in enumerate(mess_lst):
        if item.isalpha() == True:
            mess_lst[i] = output[inp.find(item)]
    return ''.join(mess_lst)



print(rot13("EBG13 rknzcyr."))

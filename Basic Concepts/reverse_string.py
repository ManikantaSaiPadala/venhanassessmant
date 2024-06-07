def reverse_string(given_str):
    res = ""
    for i in given_str:
        res = i + res 
    return res 
given_inp = input()
fin_out = reverse_string(given_inp)
print(fin_out)
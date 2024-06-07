def is_palindrome(word):
    n_w = word.lower()
    res_word = n_w[::-1]
    res = res_word == n_w
    return res 
inp_word = input()
print(is_palindrome(inp_word))
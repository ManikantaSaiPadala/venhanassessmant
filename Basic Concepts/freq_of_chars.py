inp_str = input()
new_str = set(inp_str)
new_str.discard(" ")
new_str = sorted(new_str)
res = {}
for ch in new_str:
    count = inp_str.count(ch)
    res[ch] = count 
print(res)
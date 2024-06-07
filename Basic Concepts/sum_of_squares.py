def sum_of_squares(ini_list):
    res_list = []
    for i in ini_list:
        res_list.append(i*i)
    return sum(res_list)
inp_list = list(map(int, input().split(" ")))
out_list = sum_of_squares(inp_list)
print(out_list)
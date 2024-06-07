def find_duplicates(arr):
    ori_arr = set()
    dup_arr = set()
    for num in arr:
        if num in ori_arr:
            dup_arr.add(num)
        else:
            ori_arr.add(num) 
    return list(dup_arr)

inp_arr = [1,2,2,5,7,7,8,8,9,9]
print(find_duplicates(inp_arr))
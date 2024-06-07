def merge_sort(arr):
    if len(arr) > 1:
        l_arr = arr[:len(arr)//2]
        r_arr = arr[len(arr)//2:]
        
        merge_sort(l_arr)
        merge_sort(r_arr)
        
        i = 0
        j = 0
        k = 0 
        while i<len(l_arr) and j<len(r_arr):
            if l_arr[i] < r_arr[j]:
                arr[k] = l_arr[i]
                i += 1 
            else:
                arr[k] = r_arr[j]
                j += 1 
            k += 1 
        
        while i < len(l_arr):
            arr[k] = l_arr[i]
            i += 1 
            k += 1 
        while j < len(r_arr):
            arr[k] = r_arr[j]
            j += 1 
            k += 1 
    return arr
t_arr = [1,5,9,8,7,6]
print(merge_sort(t_arr))

bin_n = format( 15 , 'b')

last_one_index = bin_n.rfind('1')

if (last_one_index <= 0):
    return 0
else:    
    bin_gap = bin_n[0:last_one_index]
    
    splitted_bin_gap = bin_gap.split("1")
    
    only_zeros = list(filter(None, splitted_bin_gap))
    
    if not only_zeros:
        return 0
    else:
        max_zeros_string = max(only_zeros, key=len)
        max_zeros_count = len(max_zeros_string)
        return max_zeros_count
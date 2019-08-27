# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(list):
    max_num = max (list) + 1
    count_list = [0] * max_num
    
    for i in range(len(list)):
        count_list[list[i]] += 1
    
    for i in range(len(count_list)):
        if (count_list[i] % 2 == 1):
            return i
            
    pass

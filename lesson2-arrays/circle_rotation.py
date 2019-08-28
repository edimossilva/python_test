# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(list, n):
    if (list == []):
        return []
    rotated_list = list.copy()
    list_count = len(list)

    if n > list_count:
        rotation = n % list_count
    else:
        rotation = n
        
    for i in range(list_count):
        if i + rotation < list_count: 
            rotation_index = i + rotation
        else:
            rotation_index = i + rotation - list_count
        rotated_list[rotation_index] = list[i] 
    return rotated_list    
    pass
    
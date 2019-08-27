def solution(A):
    list_size = len(A)
    aux_list_size = list_size + 2
    
    aux_list = [0] * aux_list_size
    for i in range(0, list_size):
        aux_list[A[i]] = 1
    
    for i in range(1, aux_list_size):
        if (aux_list[i] == 0):
            return i
    
    pass


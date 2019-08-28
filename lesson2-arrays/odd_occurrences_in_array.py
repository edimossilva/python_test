# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(list):     
    list = sorted(list)       
    for i in range(0 , len (list), 2 ):
         if i+1 == len(list):
             return list[i]
         if list[i] != list[i+1]:
             return list[i]    
    pass
   
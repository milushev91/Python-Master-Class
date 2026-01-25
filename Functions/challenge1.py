def sum_eo(n, t):
    
    start = 1 
    
    if t == "e":
        start = 2
    elif t != "o":
        return - 1
    
    sum_numbers = 0
    
    for num in range(start, n, 2):
        sum_numbers += num 
    
    return sum_numbers


print(sum_eo(10, "e"))
print(sum_eo(7, 'o'))
print(sum_eo(11, 'spam'))
        
    
    

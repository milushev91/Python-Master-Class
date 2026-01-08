low = 1 
high = 1000 
mid = low + (high - low) // 2

num_to_find = int(input(f"Number between {low} and {high}: "))

while num_to_find not in range(low, high + 1):
    num_to_find = int(input(f"Number between {low} and {high}: "))

while mid != num_to_find:
    
    if mid < num_to_find:
        low = mid + 1 
    else:
        high = mid - 1
    
    mid = low + (high - low) // 2

print(f"Number is {mid}")

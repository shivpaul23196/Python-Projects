

def second_largest(numbers):

## Not enough nums to find solution 
    if len(numbers) < 2:
        return None
    
## Remove duplicates 

    unique_nums = set(numbers)
    if len(unique_nums)<2:
        return None
    
## Initialize largest and second largest. Start with negative infinity 

    largest = second_largest = float('-inf')

    for num in unique_nums:
        if num > largest:
            second_largest = largest
            largest = num 
        elif num > second_largest:
            second_largest = num 
    
    return second_largest 


numbers = [1,4,6,9]

print(second_largest(numbers))





    




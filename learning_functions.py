def findMaxInList(numbers):
     max_value = numbers[0]
     for num in numbers:
        if num > max_value:
            max_value = num  
            
     return max_value

print(findMaxInList([12, 47, 3, 99, 23])) 

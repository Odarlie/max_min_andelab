def max_min(numbers):
    finalresult =[]
    minimum = None
    maximum = None
    for num in numbers:
        if minimum == None or num < minimum:
            minimum = num
        for num in numbers:
            if maximum == None or maximum < num :
                maximum = num
        finalresult.append(minimum)
        finalresult.append(maximum)
        return finalresult
   
  
   


    
    
        

"""
Count as spoken:

112222  ->   two one's, four 2  -> 2142

"""

44422

3422


def spoken(string):
    size = len(string)
    result = []
    freq = 0
    current = ' '
    
    for i in range(size + 1):
        if i == size or string[i] != current:            
            if freq != 0:
                result.append(str(freq))
                result.append(current)
            
            if i == size: break
                
            current = string[i]
            freq = 1
        else:
            freq += 1            
    return "".join(result)
  
    
def say_what_you_see(input_strings):
    if not input_strings: return []
    result = []
    for string in input_strings:        
        result.append(spoken(string))
    return result

        
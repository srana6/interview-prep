"""

// This is the text editor interface. 
// Anything you type or change here will be seen by the other person in real time.
/**
 * Reverse a sentence
 
“The quick brown fox”


arr = ['T', 'h', 'e', ' ', '

result: “   fox brown quick The   ”

*//

the quick brown fox

fox brown 

Time ->  O(n)
Space ->  O(1)



xof  nworb    
fox  
   

a-z A-Z


"""


def reverse(arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1


def reverse_sentense(arr):
    if not arr: return []
    arr = list(arr)
    size = len(arr)
    reverse(arr, 0, size - 1)
    
    i, j = 0, 0
    
    while j <= size:
        if j == size or arr[j] == ' ':
            reverse(arr, i, j - 1)
            j += 1
            i = j
        else:
            j += 1
    
    return arr





def reverse_sentense2(sentence):
    words = sentence.split()
    sentence_rev = " ".join(reversed(words))
    return sentence_rev
    


    
string = "    The quick brown fox    "

solution = reverse_sentense2(string)
print (solution)
    
    
        
    
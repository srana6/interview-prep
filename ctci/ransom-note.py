"""
Ransom note can be formed by cutting words out of a 
magazine to form a new sentence. 

How would you figure out if a ransom note (string) 
can be formed from a given magazine (sting)
"""

def ransom_note(ransom, magazine):
    arr_ransom = ransom.strip().split(' ')
    arr_magazine = magazine.strip().split(' ')

    print (arr_ransom)
    print (arr_magazine)

    # Hashing 
    hash_table = {}
    for word in arr_ransom:
        if word not in hash_table:
            hash_table[word] = 0
        hash_table[word] += 1

    # Processing
    for word in hash_table:
        count = 0
        for word_m in arr_magazine:
            if word == word_m:
                count += 1
        if count != hash_table[word]:
            return False
    return True


ransom = "Hi I'm Jose"
magazine = """
Hi my name is Jose and I'm from Venezuela.
"""
print (ransom_note(ransom, magazine))

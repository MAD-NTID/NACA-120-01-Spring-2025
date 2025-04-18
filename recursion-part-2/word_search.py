def find_word(target, i = 0):
    # base conditions
    if len(words) == i:
        return False
    
    if words[i] == target:
        return True
    
    # recursive conditions
    return find_word(target, i + 1)

words = [
    'flower',
    'river',
    'red',
    'apple',
    'hello',
    'sun',
    'world',
    'ocean'
]

search_for_word = "ocean"
print(f"Word '{search_for_word}' exists  {find_word(search_for_word)}")
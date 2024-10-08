def load_dictionary(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file]

def levenshtein_distance(a, b):
    """
    lev(a, b):
    -   length(a) if length(b) = 0
    -   length(b) if length(a) = 0
    -   lev(tail(a), tail(b)) if head(a) = head(b)
    -   1 + min(lev(a, tail(b)),
                lev(tail(a), b),
                lev(tail(a), tail(b))) otherwise
    """
    if len(a) == 0:
        return len(b)
    if len(b) == 0:
        return len(a)

    if a[-1] == b[-1]:
        return levenshtein_distance(a[:-1], b[:-1])
    else:
        distance_insert = levenshtein_distance(a, b[:-1])  
        distance_delete = levenshtein_distance(a[:-1], b)  
        distance_replace = levenshtein_distance(a[:-1], b[:-1]) 

        return 1 + min(distance_insert, distance_delete, distance_replace)

def spell_check(word, dictionary):
    suggestions = []
    for correct_word in dictionary:
        distance = levenshtein_distance(word, correct_word)
        suggestions.append((correct_word, distance))

    suggestions.sort(key=lambda x: x[1])
    return suggestions[:10]

dictionary = load_dictionary("spell_checker/words.txt")
misspelled_word = "wlord"
suggestions = spell_check(misspelled_word, dictionary)
for word, distance in suggestions:
    print(f"{word} (Distance: {distance})")

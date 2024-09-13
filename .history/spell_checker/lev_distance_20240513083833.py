def load_dictionary(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file]

def levenshtein_distance(a, d):
    """
    lev(a, d):
    -   length(a)
    """
    if len(a) == 0:
        return len(d)
    if len(d) == 0:
        return len(a)

    if a[-1] == d[-1]:
        return levenshtein_distance(a[:-1], d[:-1])
    else:
        cost = 1
        distance_insert = levenshtein_distance(a, d[:-1])  
        distance_delete = levenshtein_distance(a[:-1], d)  
        distance_replace = levenshtein_distance(a[:-1], d[:-1]) 

        if distance_insert <= distance_delete and distance_insert <= distance_replace:
            return distance_insert + 1
        elif distance_delete <= distance_replace:
            return distance_delete + 1
        else:
            return distance_replace + cost

def spell_check(word, dictionary):
    suggestions = []
    for correct_word in dictionary:
        distance = levenshtein_distance(word, correct_word)
        suggestions.append((correct_word, distance))

    suggestions.sort(key=lambda x: x[1])
    return suggestions[:10]

dictionary = load_dictionary("spell_checker/words.txt")
misspelled_word = "gdoo"
suggestions = spell_check(misspelled_word, dictionary)
for word, distance in suggestions:
    print(f"{word} (Distance: {distance})")

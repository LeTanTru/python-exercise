def load_dictionary(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file]

def levenshtein_distance(s1, s2):
    """
    lev(s1, s2):
    
    """
    if len(s1) == 0:
        return len(s2)
    if len(s2) == 0:
        return len(s1)

    if s1[-1] == s2[-1]:
        return levenshtein_distance(s1[:-1], s2[:-1])
    else:
        cost = 1
        distance_insert = levenshtein_distance(s1, s2[:-1])  
        distance_delete = levenshtein_distance(s1[:-1], s2)  
        distance_replace = levenshtein_distance(s1[:-1], s2[:-1]) 

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

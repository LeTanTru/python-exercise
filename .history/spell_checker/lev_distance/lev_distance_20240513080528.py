def load_dictionary(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file]

def levenshtein_distance(s1, s2):
    if len(s1) == 0:
        return len(s2), ["Insert " + c for c in s2] 
    if len(s2) == 0:
        return len(s1), ["Delete " + c for c in s1]

    if s1[-1] == s2[-1]:
        cost = 0
        distance, edits = levenshtein_distance(s1[:-1], s2[:-1])
        return distance, edits  
    else:
        cost = 1
        distance_insert, edits_insert = levenshtein_distance(s1, s2[:-1])  
        distance_delete, edits_delete = levenshtein_distance(s1[:-1], s2)  
        distance_replace, edits_replace = levenshtein_distance(s1[:-1], s2[:-1]) 

        if distance_insert <= distance_delete and distance_insert <= distance_replace:
            # edits_insert.append(f"Insert {s2[-1]}")
            return distance_insert + 1, edits_insert
        elif distance_delete <= distance_replace:
            # edits_delete.append(f"Delete {s1[-1]}")
            return distance_delete + 1, edits_delete
        else:
            # edits_replace.append(f"Substitute {s1[-1]} with {s2[-1]}")
            return distance_replace + cost

def spell_check(word, dictionary):
    suggestions = []

    for correct_word in dictionary:
        distance, edits = levenshtein_distance(correct_word, word)
        suggestions.append((correct_word, distance, edits))

    suggestions.sort(key=lambda x: x[1])
    return suggestions[:10]
distance, edits = levenshtein_distance("boat", "float") 
print(distance)  # Output: 6
print(edits)  

# dictionary = load_dictionary("spell_checker/wagner_fischer/words.txt")
# misspelled_word = "gdoo"
# suggestions = spell_check(misspelled_word, dictionary)
# for word, distance, edits in suggestions:
#     print(f"Word: {word}, Distance: {distance}")
#     print("Edits:")
#     for edit in edits:
#         print(f"  {edit}")
#     print()

dict_man = {"A": ["X", "Y", "Z"], "B": ["Z", "Y", "X"], "C": ["Z", "X", "Y"]}

dict_woman = {"X": ["B", "C", "A"], "Y": ["C", "A", "B"], "Z": ["B", "A", "C"]}


def stable_marriage(dict_man, dict_woman):
    engaged = {}
    men_free = list(dict_man.keys())

    while men_free:
        man = men_free.pop(0)
        woman = dict_man[man].pop(0)

        fiance = engaged.get(woman)

        if not fiance:
            engaged[woman] = man
        else:
            woman_pref_list = dict_woman[woman]
            if woman_pref_list.index(fiance) > woman_pref_list.index(man):
                engaged[woman] = man
                men_free.append(fiance)
            else:
                men_free.append(man)

    return engaged


engagements = stable_marriage(dict_man, dict_woman)
print("Stable Engagements:")
for woman, man in engagements.items():
    print(f"{man} engaged to {woman}")

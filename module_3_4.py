def single_root_words(root_word , *other_words):
    same_words = []
    for i in range(len(other_words)):
        if root_word.lower() == other_words[i].lower():
            same_words.append(root_word)
    print(same_words)

single_root_words("Саша", "Ваня", "Гена", "Витя", "САша")

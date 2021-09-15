import ahocorasick


def bulid_ac(wordlist):

    tree = ahocorasick.Automaton()
    for index, word in enumerate(wordlist):
        tree.add_word(word, (index, word))
    return tree.make_automaton()

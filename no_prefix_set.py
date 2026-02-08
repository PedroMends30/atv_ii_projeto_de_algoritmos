def noPrefixSet(words):
    trie = {}
    for word in words:
        current = trie
        for letter in word:
            if '_end_' in current:
                return False, word
            current = current.setdefault(letter, {})
        if current:
            return False, word
        current['_end_'] = True
    return True, None

def noPrefix(words):
    is_valid, prefix_word = noPrefixSet(words)
    if is_valid:
        print("GOOD SET")
    else:
        print("BAD SET")
        print(prefix_word)
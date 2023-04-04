from trie import Trie


def starts_with(trie, char, length):
    """
    Returns a list of all the words of length that starts with char
    """
    def find_words(current, words, current_str, max_length):
        # Recursive function for searching the word
        # When the length is reached
        if len(current_str) == max_length:
            if current.is_end:
                # Adds the word and quits recursion
                words.append(current_str)
            return
        # For every child
        for child in current.children:
            find_words(child, words, current_str + child.key, max_length)
    # Checks there if exists any word starting with char
    for child in trie.root.children:
        if child.key == char:
            break
    else:
        return
    
    words = []
    find_words(child, words, child.key, length)
    return words
    

def is_same_file(trie1, trie2):
    # Returns True if all the words of self, are inside the other Trie
    def is_contained(current_self, current_other):
        
        # When it reaches the end
        if len(current_self.children) == 0:
            return True
        for self_child in current_self.children:
            
            contained_sub_tree = False
            # If the key is contained in the other tree, just breaks
            for other_child in current_other.children:
                if self_child.key == other_child.key:
                    contained_sub_tree = is_contained(self_child, other_child)
                    break
            else:
                # When the self_child key isn't contained
                return False
            
            # If one single key is not contained in the sub_tree
            if not contained_sub_tree:
                return False
        return True
    
    return is_contained(trie1.root, trie2.root)


def get_reversed_pairs(trie):
    # Returns all the list of reversed words
    words = trie.words()
    def reversed_word(word):
        # Given a word returns the reversed version
        new_reversed = ""
        for char in reversed(word):
            new_reversed += char
        return new_reversed
    words_pairs = []
    for word in words:
        new_reversed = reversed_word(word)
        if new_reversed in words:
            words_pairs.append((word, new_reversed))
    return words_pairs


def autocompelte(trie, prefix):
    """ Given a Trie and a prefix, returns all the autocompleted words that start with the prefix"""

    """ Utility functions"""
    def _find_last_node_recursive(current, prefix, word_index):
        # Returns the node that contains the last character of the word
        # 'H' 'e' 'l' 'l' 'o'
        # Returns the noode that has the key 'o'
        if word_index == len(prefix):
            return current

        char = prefix[word_index]

        # Tries to find the child that contains the char
        for child in current.children:
            if child.key == char:
                return _find_last_node_recursive(child, prefix, word_index + 1)

        # Here, the node wasn't found, meaning the word isn't contained in the Trie

    """ Utility functions"""
    def find_words(current, words, current_str):
        # Given a node, appends the sub_tree words
        if current.is_end:
            words.append(current_str)

        # Translates recusion for all the children
        for child in current.children:
            find_words(child, words, current_str + child.key)


    """1. Finds the last node"""
    last_node = _find_last_node_recursive(trie.root, prefix, 0)

    # When the word wasn't found
    if last_node is None:
        return

    """2. Finds all the words that start with the prefix"""
    # Otherwise, traverses donwards
    words = []
    find_words(last_node, words, prefix)

    return words



if __name__ == "__main__":

    def test_general():

        trie = Trie()
        trie.insert("Buenas")
        trie.insert("B23456")
        trie.insert("Buenaspo")
        trie.insert("Abecedario")
        trie.insert("Abeja")
        trie.insert("Abejo")
        print(trie.words())
        print(trie.search("Abecedari"))
        trie.delete("Buenaspo")
        print(trie.words())
        print(trie.starts_with("A", 5))


    def test_is_same_file():
        t1 = Trie()
        t2 = Trie()

        words_t1 = ["Hola", "Buenas", "Tardes", "mucho", "gusto"]
        words_t2 = ["Hace", "calor", "hoy"]
        words_t2.extend(words_t1)

        for w in words_t1:
            t1.insert(w)

        for w in words_t2:
            t2.insert(w)

        print(is_same_file(t1, t2))

    def test_reversed_words():
        t1 = Trie()
        words_t1 = ["Hola", "Buenas", "Tardes", "mucho", "gusto", "aloH"]

        for w in words_t1:
            t1.insert(w)

        print(get_reversed_pairs(t1))

    def test_autocomplete():
        t1 = Trie()
        words_t1 = ["Hola", "Buenas", "Tardes", "mucho", "gusto", "Horario", "Horarios", "Hacias"]

        for w in words_t1:
            t1.insert(w)

        print(autocompelte(t1, "H"))

    test_is_same_file()

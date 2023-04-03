

class TrieNode:
    def __init__(self) -> None:
        self.parent = None
        self.children = []
        self.key = None
        self.is_end = False

    def link_children(self, child):
        child.parent = self
        self.children.append(child)


class Trie:
    def __init__(self) -> None:

        # The first node works as a container for all the other nodes
        self.root = TrieNode()

    def insert(self, word):
        
        # Otherwise
        char_index = 0
        self._insert_recursive(self.root, word, char_index)

    def _insert_recursive(self, current, word, char_index):
        
        # Means all the nodes were added
        if char_index >= len(word):
            return
        
        # Tries to find if the char was already added
        for child in current.children:

            # If the child has the same value (char)
            if child.key == word[char_index]:
                self._insert_recursive(child, word, char_index + 1)
                return

        # In this case, there are no children created. So it should add nodes untill it ends
        # There is no recursion needed
        word_length = len(word)
        parent = current
        while char_index < word_length:
            
            # Creates the node   
            node = TrieNode()
            node.key = word[char_index]
            
            # Links the nodes
            node.parent = parent
            parent.children.append(node)
            parent = node
            char_index += 1
        
        parent.is_end = True


    def words(self) -> list:

        def find_words(current, words, current_str):
            
            # If we find the end of a word, adds the word            
            if current.is_end:
                words.append(current_str)

            # Continues adding the rest of the word
            for child in current.children:
                find_words(child, words, current_str + child.key)

        words = []

        for child in self.root.children:
            find_words(child, words, child.key)
        
        return words

    def search(self, word):

        def _search_recursive(current, word, char_index):

            current_char = word[char_index]
            found = False

            # Tries to find a child with the same char
            for child in current.children:
                if child.key == current_char:
                    
                    # When the last char of the word was reached
                    if char_index + 1 == len(word):
                        return child.is_end

                    found = _search_recursive(child, word, char_index + 1)
                    break
            
            return found

        return _search_recursive(self.root, word, 0)
    
    def delete(self, word):

        # The word is not in the trie
        if not self.search(word): 
            return

        def _delete_recursive(current, word, char_index):
            # This code assumes that the word is contained
            current_char = word[char_index]

            # Tries to find a child with the same char
            for child in current.children:
                if child.key == current_char:
                    break

            # Child is the one that contains the current character. 

            # The end of the word is reached
            if char_index + 1 == len(word):
                
                # When child has children, just changes the end flag
                if len(child.children) != 0:
                    child.is_end = False
                    return
                
                # Here we can remove the word
                # Traverse upwards to remove the excess
                node = child
                while node is not None:
                    
                    parent = node.parent
                    # Unlinks the node, resulting in the removal of the excess of the word
                    if parent.is_end:

                        parent.children.remove(node)
                        node.parent = None
                        break
                    
                    node = parent
                
                return
            
            # Continues with the recursion until it finds the end
            _delete_recursive(child, word, char_index + 1)


        _delete_recursive(self.root, word, 0)

    def starts_with(self, char, length):
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
        for child in self.root.children:
            if child.key == char:
                break
        else:
            return
        
        words = []

        find_words(child, words, child.key, length)
        return words
    
    
    def is_same_file(self, other):
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
        
        return is_contained(self.root, other.root)


    def get_reversed_pairs(self):
        # Returns all the list of reversed words
        words = self.words()

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

        print(t1.is_same_file(t2))

    def test_reversed_words():
        t1 = Trie()
        words_t1 = ["Hola", "Buenas", "Tardes", "mucho", "gusto", "aloH"]

        for w in words_t1:
            t1.insert(w)

        print(t1.get_reversed_pairs())

    def test_autocomplete():
        t1 = Trie()
        words_t1 = ["Hola", "Buenas", "Tardes", "mucho", "gusto", "Horario", "Horarios", "Hacias"]

        for w in words_t1:
            t1.insert(w)

        print(autocompelte(t1, "H"))

    test_autocomplete()

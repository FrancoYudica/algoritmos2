

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

            current_char = word[char_index]

            # Tries to find a child with the same char
            for child in current.children:
                if child.key == current_char:
                    break

            # Child is the one that contains the current character. This code assumes that the word is contained

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


if __name__ == "__main__":
    trie = Trie()
    trie.insert("Buenas")
    trie.insert("Buenaspo")
    trie.insert("Abecedario")
    trie.insert("Abeja")
    print(trie.words())
    print(trie.search("Abecedari"))
    trie.delete("Buenaspo")
    print(trie.words())



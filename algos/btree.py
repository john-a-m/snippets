#https://en.wikipedia.org/wiki/Binary_search_tree
#http://interactivepython.org/runestone/static/pythonds/Trees/SearchTreeImplementation.html

class BTreeNode(object):

    def __init__(self, key=None, value=None, parent=None):

        self.key = key
        self.value = value
        self.parent = parent
        self.left = None
        self.right = None

    def search(self, key):

        if self.key == key:
            return self.value
        
        elif key < self.key:
            if not self.left:
                return None
            return self.left.search(key)
        
        elif key > self.key:
            if not self.right:
                return None
            return self.right.search(key)

    def traverse(self):

        if self.left:
            for node in self.left.traverse():
                yield node

        yield (self.key, self.value)

        if self.right:
            for node in self.right.traverse():
                yield node
         
    
    def insert(self, key, value):

        if not self.key or key == self.key:
            self.key = key
            self.value = value
            return None
        
        elif key < self.key:
            if self.left:
                self.left.insert(key, value)
            else:
                self.left = BTreeNode(key, value, self)
                
        else:
            if self.right:
                self.right.insert(key, value)
            else:
                self.right = BTreeNode(key, value, self)
            
    def delete(self, key):

        if key < self.key:
            self.left.delete(key)
        elif key > self.key:
            self.right.delete(key)
        elif key == self.key:
            if self.left and self.right:
                successor = self.right.min_
                self.key = successor.key
                self.value = successor.value
                successor.delete(key)
            elif self.left:
                self._replace_parent(self.left)
            elif self.right:
                self._replace_parent(self.right)
            else:
                self._replace_parent(None)
                    
    def _replace_parent(self, new):

        if self.parent:
            if self is self.parent.left:
                self.parent.left = new
            else:
                self.parent.right = new

        if new:
            new.parent = self.parent
    
    @property
    def min_(self):
        node = self
        while node.left:
            node = node.left
        return node

if __name__ == "__main__":

    btree = BTreeNode()
    for n in range(10):
        btree.insert(n, str(n))
        
    print list(btree.traverse())

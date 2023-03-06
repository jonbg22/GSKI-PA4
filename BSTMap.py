# Exception Classes

class NotFoundException(Exception):
    """Raised when key not in Tree"""
    pass

class ItemExistsException(Exception):
    """Raised when key already in Tree"""
    pass


class BSTMapNode:
    def __init__(self,key = None, data = None, left = None, right = None) -> None:
        self.key = key
        self.data = data
        self.left = left
        self.right = right

class BSTMap:
    def __init__(self, root = None) -> None:
        self.root = root


    def __str__(self) -> str:
        """
        Returns a string with the items ordered by key and separated by a single space. 
        Each item is printed on the following format: {value_of_key:value_of_data} 
        """
        return self.printInorderRecur(self.root)
        
    def printInorderRecur(self,root,out = ""):
        if root.left != None: out = self.printInorderRecur(root.left,out)
        out += f"{root.key}:{root.data} "
        if root.right != None: out = self.printInorderRecur(root.right,out)

        return out
        



    def __len__(self):
        """
        Override to allow this syntax: 
        length_of_structure = len(some_bst_map) 
        Returns the number of items in the entire data structure 
        """
        raise NotImplementedError

    def insert(self,key, data):
        """
        Adds this value pair to the collection 
        If equal key is already in the collection,raise ItemExistsException() 
        """
        self.root = self.insert_recur(key,data,self.root)

    def insert_recur(self,key,data,root):
        if root == None:
            return BSTMapNode(key,data)
        
        if key < root.key:
            root.left = self.insert_recur(key,data,root.left)
        elif key > root.key:
            root.right = self.insert_recur(key,data,root.right)
        else:
            raise ItemExistsException()

        return root


    def update(self,key, data):
        """
        Sets the data value of the value pair with equal key to data 
        If equal key is not in the collection, raise NotFoundException() 
        """
        return self.update_recur(key,data,self.root)
    
    def update_recur(self,key,data,root):
        if key == root.key:
            root.data = data
            return root
        
        if key < root.key:
            root.left = self.update_recur(key,data,root.left)
        elif key > root.key:
            root.right = self.update_recur(key,data,root.right)
        return root
        

    def find(self,key):
        """
        Returns the data value of the value pair with equal key 
        If equal key is not in the collection, raise NotFoundException() 
        """
        return self.find_recur(key,self.root)
        

    def contains(self, key):
        """
        Returns True if equal key is found in the collection, otherwise False 
        """
        return self.find(key) != None
    
    def find_recur(self, key, root):
        if root == None:
            raise NotFoundException
        if root.key == key:
            return root
        if key < root.key:
            return self.find_recur(key,root.left)
        elif key > root.key:
            return self.find_recur(key,root.right)


    def remove(self,key):
        """
        Removes the value pair with equal key from the collection 
        If equal key is not in the collection, raise NotFoundException() 
        """
        if not self.contains(key):
            raise NotFoundException
        self.root = self.remove_recur(key,self.root)
    
    def remove_recur(self, key, root):
        if root is None:
            return root

        if key < root.key:
            root.left = self.remove_recur(key,root.left)
        elif key > root.key:
            root.right = self.remove_recur(key,root.right)
        else:
            # Node is a leaf with 1 or no child
            if root.left is None:
                tmp = root.right
                root = None
                return tmp
            if root.right is None:
                tmp = root.left
                root = None
                return tmp

            # Node has two children
            successor = self.inorderSuccesor(root.right) # gets smallest node in right subtree
            root.key = successor.key
            root.data = successor.data
            root.right = self.remove_recur(successor.key,root.right) # delete successor
        
        return root
        
    def inorderSuccesor(self,root):
        # returns left most leaf
        while root.left != None:
            root = root.left
        
        return root
    
class MyComparableKey:
    
    def __init__(self, int_value, str_value):
        self.int_value = int_value
        self.str_value = str_value
    
    def __lt__(self, other):
        if isinstance(other, MyComparableKey):
            if self.int_value < other.int_value:
                return True
            elif self.int_value == other.int_value:
                return self.str_value < other.str_value
        return NotImplemented
        

if __name__ == "__main__":
    bst = BSTMap(BSTMapNode(5,"five",BSTMapNode(4,"four")))

    print(bst)

    bst.insert(3,"three")
    bst.insert(10,"ten")

    print(bst)
    bst.update(5,"FIVE")
    print(bst)
    print(bst.remove(4))
    print(bst)
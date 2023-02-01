class BST:
    def __init__(self,key = None):

        self.key = key
        self.lchild = None
        self.rchild = None

    def insert(self,value):
        self.value = value

        if self.key is None:
            self.key = value
            return
        if self.key == value:
            return

        if self.key > value:
            if self.lchild:
                self.lchild.insert(value)        
            else:
                self.lchild = BST(value)    
        else:
            if self.rchild:
                self.rchild.insert(value)        
            else:
                self.rchild = BST(value)

root = BST(30)
print(root.key)
root.lchild = BST(40)
root.rchild = BST(50)

root.insert(10)
print(root.lchild.key)
print(root.lchild.lchild.key)



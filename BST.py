#Creating a new node
class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
        
        
#For inserting a new node
def insert(d,root):
        if d<root.data:
            if root.left is None:
                root.left=Node(d)
            else:
                insert(d,root.left)
        else:
            if root.right is None:
                root.right=Node(d)
            else:
                insert(d,root.right)
    
    
    
def inorder(root):
    if root:
        print(root.value)
        inorder(root.left)
        inorder(root.right)
def printit(q,root):
    if root:
        if root.value==q:
            inorder(root)
        else:
            printit(q,root.left)
            printit(q,root.right)


#Driver code 
tree = None

nodes = int(input())
values = (input().split())
values = [int(x) for x in values]
q = int(input())

tree = Node(values[0])
for i in range(1, nodes):
    tree = insert(values[i], tree)
printit(q,tree)


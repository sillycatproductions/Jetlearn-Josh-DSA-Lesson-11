# main code start ----------------------------------------------------------------------------------------

class Tree: #tree class
    def __init__(self,a): 
        self.data = a #middle
        self.left = None #left
        self.right = None #right

def inordertravel(root): #in order of left, middle, right
    if root != None: #if root exists
        inordertravel(root.left) #read left
        print(root.data, end=" ") #read middle
        inordertravel(root.right) #read right
    
def insert(root,k): #creating a way to add to the tree
    if root is None: #if root doesn't exist
        return Tree(k) #add k value (input from the user) to the tree
    if root.data > k: #if middle is bigger than k
        root.left = insert(root.left, k) #add k to the left
    else:
        root.right = insert(root.right, k) #if its smaller add k to the right
    return root #idk

def delete(root, key): #creating a way to delete values from the tree
    if root is None: #if root doesn't exist
        return root #idk
    if key < root.data: #if value you want to delete is smaller than middle
        root.left = delete(root.left, key) #delete from the left
    elif key > root.data: #if value you want to delete is bigger than middle
        root.right = delete(root.right, key) #delete the right
    else: # 3 conditions of deleting here -------------------------------------------------------------------------
        if root.left is None and root.right is None: #if parent node has no children
            return None #don't delete anything except the parent
        
        elif root.left is None: #if parent node only has right child
            temr = root.right #temporary value
            root = None #delete root
            return temr #directly add temporary value to the parent
        elif root.right is None: #if parent node only has left child
            temr = root.left #line 36
            root = None #line 37
            return temr #line 38
        
        temr = minValueNode(root.right) #if parent node has 2 children
        root.data = temr.data
        root.right = delete(root.right, temr.data)
        
    return root

def minValueNode(node): #minimum value
    current = node
    while current.left != None:
        current = current.left
    return current
# 3 conditions end here ----------------------------------------------------------------------------------------

# main code end ------------------------------------------------------------------------------------

ya = int(input('Enter the amount of elements you want in the tree: '))
root = None
for i in range(ya):
    x = int(input('Name the element: '))
    root = insert(root, x)

print('Elements before deletion: ')
inordertravel(root)

num = int(input(' \n Enter the amount of elements you want to delete: '))
for i in range(num):
    dele = int(input('Delete an element in the undeleted list: '))
    root = delete(root, dele)

print('Elements after deletion: ')
inordertravel(root)


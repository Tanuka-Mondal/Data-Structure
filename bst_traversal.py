class BST:
  def __init__(self,node) :
    self.node = node
    self.leftnode = None
    self.rightnode = None

  def insert(self,value)  :
    if self.node is None: #if tree is empty
      self.node = value   #the value will be assigned to the root
    elif self.node > value  : 
      if self.leftnode: #if left child node contains data
        self.leftnode.insert(value) #recursion will happen for the left sub tree
      else:  #if left subtree is empty
        self.leftnode = BST(value)  #create a new node
    elif self.node < value  : 
      if self.rightnode: #if right child node contains data
        self.rightnode.insert(value) #recursion will happen for the right sub tree
      else:  #if right subtree is empty
        self.rightnode = BST(value)  #create a new node  
    else:
      return #if duplicate value, ignore 
  
  def preorder(self)     :     
    print(self.node, end = " ")  
    if self.leftnode:
      self.leftnode.preorder() 
    if self.rightnode:
      self.rightnode.preorder()  
  
  def inorder(self)     :      
    if self.leftnode:
      self.leftnode.inorder()
    print(self.node, end = " ")  
    if self.rightnode:
      self.rightnode.inorder()  

  def postorder(self)     :      
    if self.leftnode:
      self.leftnode.postorder() 
    if self.rightnode:
      self.rightnode.postorder()  
    print(self.node, end = " ")      
    
newTree = BST(50)
lst = [10,20,70,60,65,5,30,100,55,25]
for i in lst:
  newTree.insert(i)
  
print("Pre-order Traversal")
newTree.preorder()
print("\n\nIn-order Traversal")
newTree.inorder()
print("\n\nPost-order Traversal")
newTree.postorder()

"""
Pre-order Traversal
50 10 5 20 30 25 70 60 55 65 100 

In-order Traversal
5 10 20 25 30 50 55 60 65 70 100 

Post-order Traversal
5 25 30 20 10 55 65 60 100 70 50 
"""
    

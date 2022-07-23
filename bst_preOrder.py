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
      
tree = BST(15)

l = [2,6,8,20,1,4,60,35]
for i in l:
  tree.insert(i)
  
tree.preorder()
"""
15 2 1 6 4 8 20 60 35 
"""

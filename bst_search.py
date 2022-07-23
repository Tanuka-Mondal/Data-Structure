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
      
  def search(self,value)  :
      if self.node == value:
        print("Data is present")
      elif self.node > value:
        if self.leftnode:
          self.leftnode.search(value) 
        else:
          print("Data is not present")  
      else:   #self.node < value
         if self.rightnode:
           self.rightnode.search(value) 
         else:
           print("Data is not present")     
            

tree = BST(15)

l = [2,6,8,1,4,35]
for i in l:
  tree.insert(i)
  
tree.search(2)  
tree.search(60)     
tree.search(15)
tree.search(1)   

"""
Data is present
Data is not present
Data is present
Data is present
"""

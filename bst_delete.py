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

  def inorder(self)     :      
    if self.leftnode:
      self.leftnode.inorder()
    print(self.node, end = " ")  
    if self.rightnode:
      self.rightnode.inorder()     

  def delete(self,value)    :
    if self.node is None:
      print("Tree is empty")   
      return  
    if value < self.node:
      if self.leftnode:
        self.leftnode = self.leftnode.delete(value)    
      else:
        print("Node is not present in tree")
    elif value > self.node:
      if self.rightnode:
        self.rightnode = self.rightnode.delete(value)    
      else:
        print("Node is not present in tree")      
    else:   #data is equal to root node
      if self.leftnode is None:
        temp = self.rightnode #store the value of rightnode in temp
        self = None #delete the node
        return temp #return the rightnode
      if self.rightnode is None:
        temp = self.leftnode #store the value of leftnode in temp
        self = None #delete the node
        return temp #return the lefttnode
      #these two are for if a node contain 0 child or 1 child
      flag = self.rightnode #because in case of 2 child we want to replace with smallest child of right sub tree
      while flag.leftnode:  #while there leftnode is present
        flag = flag.leftnode  
        self.node = flag.node #the node to be deleted is replaced by the smallest node of RST
        self.rightnode =   self.rightnode.delete(flag.node) #now change the right node
    return self  
      
    
    
tree = BST(15)

l = [2,6,8,1,4,35]
for i in l:
  tree.insert(i)
  
tree.inorder()
#1 2 4 6 8 15 35 

tree.delete(4)
tree.inorder()
#1 2 6 8 15 35 

class BST:
  def __init__(self,node) :
    self.node = node
    self.leftnode = None
    self.rightnode = None
    
root = BST(28)
print(root.node)
print(root.leftnode)
print(root.rightnode)
"""
28
None
None
"""

root.leftnode = BST(17)
print(root.leftnode.node)
print(root.leftnode.leftnode)
print(root.leftnode.rightnode)
"""
17
None
None
"""

print(root.node)
print(root.leftnode)
print(root.rightnode)
"""
28
<__main__.BST object at 0x7f071c7f7bd0>
None
"""

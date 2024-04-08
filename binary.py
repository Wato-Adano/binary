class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def inOrderTraversal(node):
        if node is None:
            return
    inOrderTraversal(node.left)
    print(node.data, end=", ")
    inOrderTraversal(node.right)

root = TreeNode('R')
nodeA = TreeNode('A')
nodeB = TreeNode('B')
nodeC = TreeNode('C')
nodeD = TreeNode('D')
nodeE = TreeNode('E')
nodeF = TreeNode('F')
nodeG = TreeNode('G')

root.left = nodeA
root.right = nodeB

nodeA.left = nodeC
nodeA.right = nodeD

nodeB.left = nodeE
nodeB.right = nodeF

nodeF.left = nodeG
 
inOrderTraversal(root)
  
  
class newNode:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None
 


 
 
def findMax(root):
 
              if (root == None):
                  return float('-inf')
 
   
res = root.data
lres = findMax(root.left)
rres = findMax(root.right)
if (lres > res):
        res = lres
if (rres > res):
        res = rres
     return res
 
 
if __name__ == '__main__':
    root = newNode(2)
    root.left = newNode(7)
    root.right = newNode(5)
    root.left.right = newNode(6)
    root.left.right.left = newNode(1)
    root.left.right.right = newNode(11)
    root.right.right = newNode(9)
    root.right.right.left = newNode(4)
 

    print("Maximum element is",
          findMax(root))
 
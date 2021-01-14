class Node:
    def __init__(self,node):
        self.left=None
        self.right=None
        self.value=node

def insert(root,node):
    if root is None:
        root=node
    else:
        if node.value<root.value:
            if root.left is None:
                root.left=node
            else:
                insert(root.left,node)
        elif node.value>root.value:
            if root.right is None:
                root.right=node
            else:
                insert(root.right,node)

def inorder(root):
    if root:
        inorder(root.left)
        print(root.value,end=" ")
        inorder(root.right)
def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.value,end=" ")
def preorder(root):
    if root:
        print(root.value,end=" ")
        preorder(root.left )
        preorder(root.right)


def minimum(node):
    current=node
    while current.left is not None:
        current=current.left
    return current

def deletion(root,node):
    if root in None:
        return None
    elif node<root.value:
        root.left=deletion(root.left,node)
    elif node>root.value:
        root.right=deletion(root.right,node)
    else:
        if root.left is None:
            temp=root.right
            root=None
            return temp
        elif root.right is None:
            temp=root.left
            root=None
            return temp
        temp=minimum(root.right)
        root.value=temp.value
        root.right=deletion(root.right,temp.value)
    return root


r=Node(14)
insert(r,Node(10))
insert(r,Node(17))
insert(r,Node(12))
insert(r,Node(11))
insert(r,Node(20))
insert(r,Node(18))
insert(r,Node(25))
insert(r,Node(8))
insert(r,Node(23))
print("inorder:",end=" ")
inorder(r)
print("\npostrder:",end=" ")
postorder(r)
print("\npreorder:",end=" ")
preorder(r)


x=deletion(r,10)
print("\nafter deletion",end=" ")
inorder(r)

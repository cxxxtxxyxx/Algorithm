import sys

input = sys.stdin.readline

class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    @staticmethod
    def find_node(node, value):
        if node == None:
            return
        if node.value == value:
            return node
        
        findN = Node.find_node(node.left, value)
        if findN != None and findN.value == value:
            return findN

        

        return Node.find_node(node.right, value)

    @staticmethod
    def pre_order(node):
        if node == None:
            return
        

        print(node.value, end="")
        Node.pre_order(node.left)
        Node.pre_order(node.right)

    @staticmethod
    def in_order(node):
        if node == None:
            return
        
        Node.in_order(node.left)
        print(node.value, end="")
        Node.in_order(node.right)

    @staticmethod
    def post_order(node):
        if node == None:
            return
        
        Node.post_order(node.left)
        Node.post_order(node.right)
        print(node.value, end="")


n = int(input())
root = 0
for i in range(n):
    if i == 0:
        root, left, right = input().strip().split()

        root = Node(root)
        if left != '.':
            root.left = Node(left)
        if right != '.':
            root.right = Node(right)

    else:
        find, left, right = input().strip().split()
        find_node = Node.find_node(root, find)
        if left != '.':
            find_node.left = Node(left)
        if right != '.':
            find_node.right = Node(right)

Node.pre_order(root)
print()
Node.in_order(root)
print()
Node.post_order(root)
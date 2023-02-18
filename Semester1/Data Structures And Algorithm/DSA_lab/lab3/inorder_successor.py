class Node:
    
	def __init__(self, data, left=None, right=None):
		self.data = data
		self.left = left
		self.right = right



def insert(root, key):
	if root is None:
		return Node(key)
	if key < root.data:
		root.left = insert(root.left, key)
	else:
		root.right = insert(root.right, key)
	return root


def min(root):
	while root.left:
		root = root.left
	return root


def inorder_successor(root, successor, key):
	if root is None:
		return successor

	
	if root.data == key:
		if root.right:
			return min(root.right)
	elif key < root.data:
		successor = root
		return inorder_successor(root.left, successor, key)
	else:
		return inorder_successor(root.right, successor, key)
	return successor


if __name__ == '__main__':
	keys = [18, 6, 21, 3, 11, 9, 13]

	

	root = None
	for key in keys:
		root = insert(root, key)

	
	for key in keys:
		successor = inorder_successor(root, None, key)

		if successor:
			print(f'The successor of node {key} is {successor.data}')
		else:
			print(f'No Successor exists for node {key}')

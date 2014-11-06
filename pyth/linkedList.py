class Node(object):
	def __init__(self, data):
		self.data = data
		self.nextNode = None 

class linkedList(object):
		def __init__(self, head=None):
				self.head = head

		def insert(self, node):
				if not self.head:
					self.head = node
				else:
					node.nextNode = self.head
					self.head = node
		def search(self, lList, Node):
				if self.head == Node:
						return self.head
				else:
					if lList.head.nextNode:
						self.search(linkedList(lList.head.nextNode), Node)
					else:
						raise ValueError("Node not in Linked List")

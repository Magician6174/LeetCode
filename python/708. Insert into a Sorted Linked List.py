# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
	def insert(self,head,insertVal):
	"""
	:type head: Node
	:type insertVal: int
	:rtype: Node
	"""
	if head == None:
		newNode = Node(insertVal, None)
		newNode.next = newNode
		return newNode
	prev, current = head, head.next
	toInsert = False
	while True:
		
		if prev.val <= insertVal <= current.val:
			toInsert = True
		
		elif prev.val > current.val:
			if perv.val < insertVal or current.val > insertVal:
				toInsert = True
		
		if toInsert:
			prev.next = Node(insertVal, current)
			return head
		
		prev, current = current, current.next
		
		if prev == head:
			break
	
	# for case like [3,3,3,3] and insertVal = 10
	prev.next = Node(insertVal, current)
	return head
		

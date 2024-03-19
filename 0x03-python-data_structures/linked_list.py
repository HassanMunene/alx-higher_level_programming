#!/usr/bin/python3

# define a class that will have the blueprint of the node i.e the value and the next
class LinkNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

#create node objects and later link them they are integers

node1 = LinkNode(1)
node2 = LinkNode(3)
node3 = LinkNode(2)
node4 = LinkNode(2)
node5 = LinkNode(3)
node6 = LinkNode(1)

# then connect the nodes to create a linked list of the nodes
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
node6.next = None

# iterate throught the linked list while printing the values
currentNode = node1

while currentNode != None:
    print(currentNode.value, end=' ')
    currentNode = currentNode.next
print()

def is_palindrom(head):
    def findMiddleNode():
        slow = head
        fast = head
        while (fast and fast.next):
            fast = fast.next.next
            slow = slow.next
        return slow

    def reverse_secondHalf(head):
        prev = None
        while head:
            temp = head.next
            head.next = prev
            prev = head
            head = temp
        return prev

    def compare_firstHalf_secondHalf_lists(firstList, secondList):
        while firstList and secondList:
            print(firstList.value, secondList.value)
            if firstList.value != secondList.value:
                return False
            firstList = firstList.next
            secondList = secondList.next
        return True


    middle_node = findMiddleNode()
    secondHalf_head = reverse_secondHalf(middle_node.next)
    print(secondHalf_head.value)
    return compare_firstHalf_secondHalf_lists(node1, secondHalf_head)

value = is_palindrom(node1)
print(value)

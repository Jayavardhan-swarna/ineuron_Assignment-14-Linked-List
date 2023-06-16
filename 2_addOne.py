class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def reverseLinkedList(head):
    prev = None
    current = head

    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node

    return prev

def addOne(head):
    # Reverse the linked list
    head = reverseLinkedList(head)

    # Initialize carry as 1
    carry = 1
    current = head

    while current:
        # Add carry to the current node's value
        sum = current.data + carry

        if sum < 10:
            # Update the node's value and break the loop
            current.data = sum
            break
        else:
            # Set the node's value to 0 and continue to the next node
            current.data = 0
            current = current.next

    # If the carry is still 1 at the end, create a new node with value 1
    if carry == 1:
        new_node = Node(1)
        current.next = new_node

    # Reverse the linked list again
    head = reverseLinkedList(head)

    return head

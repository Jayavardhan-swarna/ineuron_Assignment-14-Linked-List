class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.random = None

def copyRandomList(head):
    if head is None:
        return None

    # Step 1: Create a mapping dictionary
    mapping = {}

    # Step 2: Initialize pointers
    current = head
    newHead = None

    # Step 3: Create new nodes and store mapping
    while current:
        newNode = Node(current.data)
        mapping[current] = newNode

        if newHead is None:
            newHead = newNode

        current = current.next
        newNode = newNode.next

    # Step 4: Set current pointer back to the head
    current = head

    # Step 5: Set random pointers
    while current:
        newNode = mapping[current]
        newNode.random = mapping.get(current.random)

        current = current.next
        newNode = newNode.next

    # Step 6: Return the newHead
    return newHead

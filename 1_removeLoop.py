class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def removeLoop(head):
    if head is None or head.next is None:
        return head

    slowPtr = head
    fastPtr = head

    # Detect the loop
    while fastPtr and fastPtr.next:
        slowPtr = slowPtr.next
        fastPtr = fastPtr.next.next
        if slowPtr == fastPtr:
            break

    # If there is no loop, return the list as it is
    if slowPtr != fastPtr:
        return head

    # Move slowPtr to the head and find the node where the loop starts
    slowPtr = head
    while slowPtr.next != fastPtr.next:
        slowPtr = slowPtr.next
        fastPtr = fastPtr.next

    # Remove the loop by making the next pointer null
    fastPtr.next = None

    return head

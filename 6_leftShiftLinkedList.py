class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def leftShiftLinkedList(head, k):
    if head is None or head.next is None:
        return head

    # Step 2: Find the length of the linked list
    length = 0
    temp = head
    while temp:
        length += 1
        temp = temp.next

    # Step 3: Normalize the value of k
    k %= length

    # Step 4: If k is 0, return the head as it is
    if k == 0:
        return head

    # Step 5: Initialize pointers
    fast = head
    slow = head

    # Step 6: Move the fast pointer k steps ahead
    for _ in range(k):
        fast = fast.next

    # Step 7: Move both pointers simultaneously
    while fast.next:
        fast = fast.next
        slow = slow.next

    # Step 8: Set the next pointer of the last node to the head
    fast.next = head

    # Step 9: Set the head of the linked list to the next node of the slow pointer
    head = slow.next

    # Step 10: Set the next pointer of the slow pointer to None
    slow.next = None

    # Step 11: Return the head of the modified linked list
    return head

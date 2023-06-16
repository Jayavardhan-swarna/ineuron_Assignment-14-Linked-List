class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def oddEvenList(head):
    if head is None or head.next is None:
        return head

    # Step 2: Initialize pointers
    odd = head
    even = head.next
    evenHead = even

    # Step 3: Connect odd nodes and even nodes separately
    while even and even.next:
        odd.next = even.next
        odd = odd.next
        even.next = odd.next
        even = even.next

    # Step 4: Connect the odd and even lists
    odd.next = evenHead

    # Step 5: Return the head of the modified list
    return head

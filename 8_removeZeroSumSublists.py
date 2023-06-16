class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeZeroSumSublists(head):
    dummy = ListNode(0)
    dummy.next = head

    prefix_sum = 0
    prefix_sum_dict = {0: dummy}

    while head:
        prefix_sum += head.val

        if prefix_sum in prefix_sum_dict:
            # Remove nodes from previous node to current node
            prev = prefix_sum_dict[prefix_sum]
            prev.next = head.next

            # Update prefix sums in the dictionary
            temp = prefix_sum + prev.next.val
            while temp != prefix_sum:
                del prefix_sum_dict[temp]
                prev = prev.next
                temp += prev.next.val
            continue

        prefix_sum_dict[prefix_sum] = head
        head = head.next

    return dummy.next

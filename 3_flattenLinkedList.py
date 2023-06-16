class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.bottom = None

def mergeLists(list1, list2):
    # Base cases
    if list1 is None:
        return list2
    if list2 is None:
        return list1

    # Merge the two lists in sorted order
    if list1.data < list2.data:
        result = list1
        result.bottom = mergeLists(list1.bottom, list2)
    else:
        result = list2
        result.bottom = mergeLists(list1, list2.bottom)

    return result

def class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.bottom = None

def mergeLists(list1, list2):
    # Base cases
    if list1 is None:
        return list2
    if list2 is None:
        return list1

    # Merge the two lists in sorted order
    if list1.data < list2.data:
        result = list1
        result.bottom = mergeLists(list1.bottom, list2)
    else:
        result = list2
        result.bottom = mergeLists(list1, list2.bottom)

    return result

def flattenLinkedList(head):
    # Base case: empty list or the next pointer is None
    if head is None or head.next is None:
        return head

    # Recursively flatten the next pointer
    head.next = flattenLinkedList(head.next)

    # Merge the flattened next pointer with the current node's bottom pointer
    head = mergeLists(head, head.next)

    return head
(head):
    # Base case: empty list or the next pointer is None
    if head is None or head.next is None:
        return head

    # Recursively flatten the next pointer
    head.next = flattenLinkedList(head.next)

    # Merge the flattened next pointer with the current node's bottom pointer
    head = mergeLists(head, head.next)

    return head

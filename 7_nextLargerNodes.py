class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def nextLargerNodes(head):
    if head is None or head.next is None:
        return []

    # Step 2: Convert the linked list into an array
    arr = []
    while head:
        arr.append(head.val)
        head = head.next

    length = len(arr)
    answer = [0] * length
    stack = []

    # Step 5: Traverse the array from right to left
    for i in range(length - 1, -1, -1):
        # Pop elements from the stack
        while stack and arr[i] >= arr[stack[-1]]:
            stack.pop()

        # Update the answer array with the next greater element
        if stack:
            answer[i] = arr[stack[-1]]

        # Push the current index onto the stack
        stack.append(i)

    return answer

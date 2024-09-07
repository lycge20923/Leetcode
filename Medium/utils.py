
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def createListNode(array):
    if not array:
        return None
    node = head = ListNode(array[0])
    for ele in array[1:]:
        node.next = ListNode(ele)
        node = node.next
    return head

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def createTreeNode(array):
    if not array or array[0] is None:
        return None
    
    root = TreeNode(array[0])
    queue = [root]
    index = 1
    
    while index < len(array):
        current = queue.pop(0)

        if index < len(array) and array[index] is not None:
            current.left = TreeNode(array[index])
            queue.append(current.left)
        index += 1
        
        if index < len(array) and array[index] is not None:
            current.right = TreeNode(array[index])
            queue.append(current.right)
        index += 1
    return root
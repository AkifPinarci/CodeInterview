class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

    def print(self):
        while self:
            print(self.val, end=' ')
            self = self.next
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

def mergeTwoLists(list1, list2):
        result = ListNode(-1)
        track = result
        while list1 and list2:
            if list1.val < list2.val:
                track.next =list1
                list1 = list1.next
            else:
                track.next = list2
                list2 = list2.next
            track = track.next
        # while list1:
        #     track.next = list1
        #     list1= list1.next
        # while list2:
        #     track.next = list2
        #     list2 = list2.next
        track.next = list1 or list2
        return result.next

def reverse(node):
    return reverseHelp(head, None)



def reverseHelp(head, new):
    if head is None:
        return new
    next = head.next
    head.next = new
    return reverseHelp(next, head)

node = reverse(head)

mergeTwoLists(head, node).print()
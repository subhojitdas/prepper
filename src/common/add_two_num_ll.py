# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        if l1 is None and l2 is None:
            return None
        if l1 is None:
            return l2
        if l2 is None:
            return l1

        t1 = l1
        t2 = l2
        carry = 0
        prev = None
        res_start = None
        while t1 is not None and t2 is not None:
            cv1 = t1.val
            cv2 = t2.val
            new_val = cv1 + cv2 + carry
            if new_val >= 10:
                carry = new_val // 10
                new_val = new_val % 10
            else:
                carry = 0
            new_node = ListNode(new_val)
            if prev is not None:
                prev.next = new_node
                prev = new_node
            else:
                res_start = new_node
                prev = new_node
            t1 = t1.next
            t2 = t2.next

        n1 = t1
        if t1 is None:
            n1 = t2

        while n1 is not None:
            new_val = n1.val + carry
            if new_val >= 10:
                carry = new_val // 10
                new_val = new_val % 10
            new_node = ListNode(new_val)
            prev.next = new_node
            prev = new_node
            n1 = n1.next

        if carry > 0:
            new_node = ListNode(carry)
            prev.next = new_node

        return res_start



ln11, ln12, ln13 = ListNode(9), ListNode(9), ListNode(9)
ln11.next = ln12
ln12.next = ln13

# ln21, ln22, ln23 = ListNode(9), ListNode(6), ListNode(4)
# ln21.next = ln22
# ln22.next = ln23

ln21 = ListNode(9)

ret = Solution().addTwoNumbers(ln11, ln21)

while ret is not None:
    print(ret.val)
    ret = ret.next






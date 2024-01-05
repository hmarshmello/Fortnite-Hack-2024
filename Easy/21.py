class Solution:
    def mergeTwoLists(self, list1,list2):
        cur = head = ListNode()
        while list1 and list2:
            if list1.val < list2.val:
                cur.next = list1
                cur = list1
                list1 = list1.next
            else:
                cur.next = list2
                cur = list2
                list2 = list2.next
        cur.next = list1 or list2
        return head.next
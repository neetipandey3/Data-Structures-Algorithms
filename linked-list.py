# Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class LinkedList:
    def delete_node(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next

    def remove_nth_from_end(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """

        if n == 0:
            return head

        pointer1 = pointer2 = head

        for i in range(n):
            pointer2 = pointer2.next

        # when the list has exactly n elements
        if pointer2 == None:
            head = head.next
        else:
            while pointer2.next != None:
                pointer2 = pointer2.next
                pointer1 = pointer1.next
                # if pointer2.next == None:
                # break

            pointer1.next = pointer1.next.next

        return head

    def merge_two_sorted_lists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l3 = ListNode(0)
        ptr_0 = l3
        while l1 and l2:
            if l1.val > l2.val:
                l3.next = l2
                l2 = l2.next
            else:
                l3.next = l1
                l1 = l1.next

            l3 = l3.next

        if l2:
            l3.next = l2
        if l1:
            l3.next = l1

        return ptr_0.next

    def reverse_list(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev = None
        while head:
            this = head
            head = head.next
            this.next = prev
            prev = this

        return prev
    def print_linked_list(self, l):
        while l is not None:
            print(l.val)
            l = l.next

    def has_cycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

        #Floyd's Cycle Detection Algorithm
        if not head:
            return False

        slow = fast = head
        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        '''
        You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
        
        You may assume the two numbers do not contain any leading zero, except the number 0 itself.
        
        Example:
        
        Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
        Output: 7 -> 0 -> 8
        Explanation: 342 + 465 = 807.
        '''
        dummy = cur = ListNode(0)
        carry = 0
        while l1 or l2 or carry:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next
            cur.next = ListNode(carry % 10)
            cur = cur.next
            carry //= 10
        return dummy.next

    def odd_even_list(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        '''Given a singly linked list, group all odd nodes together followed by the even nodes. Please note here we are talking about the node number and not the value in the nodes.

        You should try to do it in place. The program should run in O(1) space complexity and O(nodes) time complexity.
        
        Example 1:
        
        Input: 1->2->3->4->5->NULL
        Output: 1->3->5->2->4->NULL
        Example 2:
        
        Input: 2->1->3->5->6->4->7->NULL
        Output: 2->3->6->7->1->5->4->NULL
        Note:
        
        The relative order inside both the even and odd groups should remain as it was in the input.
        The first node is considered odd, the second node even and so on ...'''
        if not head or not head.next:
            return head
        odd_head = odd = head
        even_head = even = head.next
        while odd.next and even.next:
            odd.next = odd.next.next
            odd = odd.next

            even.next = even.next.next
            even = even.next

        odd.next = even_head
        return odd_head


def main():

    #test merge_two_sorted_lists
    ll = LinkedList()
    l1 = ListNode(1)
    ll1 = l1
    l1.next = ListNode(4)
    l2 = ListNode(-3)
    ll2 = l2
    l2.next = ListNode(1)
    l2 = l2.next
    l2.next = ListNode(2)

    l = ll.merge_two_sorted_lists(ll1, ll2)
    ll.print_linked_list(l)



if __name__ == "__main__":
    main()





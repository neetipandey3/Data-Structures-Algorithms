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





'''

Singly Linked List

Given a linked list, remove the n-th node from the end of list and return its head.

Example:

Given linked list: 1->2->3->4->5, and n = 2.

After removing the second node from the end, the linked list becomes 1->2->3->5.
Note:

Given n will always be valid.

Follow up:

Could you do this in one pass?
'''


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def traverse(self):
        node = self  # start from the head node
        while node != None:
            print(node.val)  # access the node value
            node = node.next  # move on to the next node

class SinglyLinkedList:
   # def __init__(self):
      #  self.head = None
    #def addNodes(self, val):
       # node = ListNode(val)
       # node.next = self.head.next  # link the new node to the 'previous' node.
       # self.head.next = node
    def removeNode(self, head: ListNode, n: int):

        if n==0:
            return head

        pointer1 = pointer2 = head

        for i in range(0, n):
            pointer2 = pointer2.next

        #when the list has exactly n elements
        if pointer2 == None:
            head = head.next
        while pointer2.next != None:
            pointer2 = pointer2.next
            pointer1 = pointer1.next
           # if pointer2.next == None:
                #break

        pointer1.next = pointer1.next.next

        return head


def main():
    sll = SinglyLinkedList()
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(5)

    head = node1
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    print(sll.removeNode(head, 2).traverse())

if __name__ == "__main__":
    main()




'''
Implement a data structure supporting the following operations:

Inc(Key) - Inserts a new key with value 1. Or increments an existing key by 1. Key is guaranteed to be a non-empty string.
Dec(Key) - If Key's value is 1, remove it from the data structure. Otherwise decrements an existing key by 1. If the key does not exist, this function does nothing. Key is guaranteed to be a non-empty string.
GetMaxKey() - Returns one of the keys with maximal value. If no element exists, return an empty string "".
GetMinKey() - Returns one of the keys with minimal value. If no element exists, return an empty string "".
Challenge: Perform all these in O(1) time complexity.


'''
from collections import defaultdict

#    Doubly-Linked-List Node
#       A DLL will be maintained with a sorted set of nodes
#       with the head node containing ints/strings with the least frequency
#       and the tail node with the highest
class Node:
    def __init__(self):
        self.keys = set([])
        self.next = None
        self.prev = None

    def add_key(self, key):
        self.keys.add(key)

    def remove_key(self, key):
        self.keys.remove(key)

    def is_empty(self):
        return len(self.keys) == 0

    def get_a_key(self):
        if self.keys:
            key = self.keys.pop()
            self.keys.add(key)
            return key
        else:
            return ""
    def count(self):
        return len(self.keys)

class DoublyLinkedList:
    def __init__(self):
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def insert_after(self, x):
        node = Node()
        save_x_next = x.next
        x.next = node
        node.prev = x
        node.next = save_x_next
        save_x_next.prev = node
        return node

    def insert_before(self, x):
        return self.insert_after(x.prev)

    def remove(self, x):
        save_x_prev = x.prev
        save_x_prev.next = x.next
        x.next.prev = save_x_prev

    def get_head(self):     #the sentinel head node
        return self.head

    def get_tail(self):     #the sentinel tail node
        return self.tail

    def get_first_node(self):
        return self.head.next

    def get_last_node(self):
        return self.tail.prev



class AllOne:



    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dll = DoublyLinkedList()
        self.key_bucket_hash = defaultdict(int) # hashmap which helps inc or dec key frequency in O(1)
        self.node_freq_hash = {0: self.dll.get_head()} #a hashmap which maps an int to a bucket node

    def rmv_prev_freq_node(self, prev_freq, key):
        node = self.node_freq_hash[prev_freq]
        node.remove_key(key)
        if node.is_empty():
            self.dll.remove(node)
            self.node_freq_hash.pop(prev_freq)


    def inc(self, key):
        """
        Inserts a new key <Key> with value 1. Or increments an existing key by 1.
        :type key: str
        :rtype: void
        """
        prev_freq = self.key_bucket_hash[key]
        self.key_bucket_hash[key] += 1
        curr_freq = self.key_bucket_hash[key]

        if curr_freq not in self.node_freq_hash:
            self.node_freq_hash[curr_freq] = self.dll.insert_after(self.node_freq_hash[prev_freq])

        self.node_freq_hash[curr_freq].add_key(key)

        if prev_freq > 0:
            self.rmv_prev_freq_node(prev_freq, key)






    def dec(self, key):
        """
        Decrements an existing key by 1. If Key's value is 1, remove it from the data structure.
        :type key: str
        :rtype: void
        """
        if key in self.key_bucket_hash:
            prev_freq = self.key_bucket_hash[key]
            self.key_bucket_hash[key] -= 1
            print(self.key_bucket_hash)
            curr_freq = self.key_bucket_hash[key]
            if self.key_bucket_hash[key] == 0:
                self.key_bucket_hash.pop(key)

            if curr_freq != 0:
                if curr_freq not in self.node_freq_hash:
                    self.node_freq_hash[curr_freq] = self.dll.insert_before(self.node_freq_hash[prev_freq])
                self.node_freq_hash[curr_freq].add_key(key)
            self.rmv_prev_freq_node(prev_freq, key)


    def getMaxKey(self):
        """
        Returns one of the keys with maximal value.
        :rtype: str
        """
        return self.dll.get_last_node().get_a_key()
    def getMinKey(self):
        """
        Returns one of the keys with Minimal value.
        :rtype: str
        """

        return self.dll.get_first_node().get_a_key()

def main():

    #Your AllOne object will be instantiated and called as such:
    obj = AllOne()
    obj.inc("getMaxKey")
    obj.inc("getMaxKey")
    obj.inc("getMaxKey")
    obj.inc("getMinKey")
    obj.dec("AllOne")
    print(obj.getMaxKey())
    print(obj.getMinKey())

if __name__ == "__main__":
    main()


        # Your AllOne object will be instantiated and called as such:
        # obj = AllOne()
        # obj.inc(key)
        # obj.dec(key)
        # param_3 = obj.getMaxKey()
        # param_4 = obj.getMinKey()
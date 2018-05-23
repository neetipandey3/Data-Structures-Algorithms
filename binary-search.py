'''
Binary Search Problem


Binary Search: Search a sorted array by repeatedly dividing the search interval in half.
Begin with an interval covering the whole array. If the value of the search key is less than
 the item in the middle of the interval, narrow the interval to the lower half.
 Otherwise narrow it to the upper half. Repeatedly check until the value is found or the interval is empty.


The idea of binary search is to use the information that the array is sorted and reduce
the time complexity to O(Log n).
'''
class BinarySearch:
    def binary_search(self, num_list: list, num_to_search: int, l_pivot: int, r_pivot: int):
        if r_pivot == 0:
            return -1

        # Look for the middle index in the list to cut the search list into half as long
        mid_idx = 1 + (r_pivot - 1) // 2

        if num_to_search == num_list[mid_idx]:
            return mid_idx

        if num_to_search > num_list[mid_idx]:
            return self.binary_search(num_list, num_to_search, mid_idx + 1, r_pivot)
        else:
            return self.binary_search(num_list, num_to_search, l_pivot, mid_idx)


def main():
    bSearch = BinarySearch()
    num_list = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
    num_to_search = 23
    searched_idx = bSearch.binary_search(num_list, num_to_search, 0, len(num_list) - 1)
    if searched_idx != -1:
        print("Found the number {} at index {}".format(num_to_search, searched_idx))
    else:
        print("Number not found!")

if __name__ == "__main__":
    main()
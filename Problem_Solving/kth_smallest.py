
def kth(a_list, k):
    return _kth(a_list, 0, len(a_list)-1, k)


def _kth(a_list, l, r, k):
    p_idx = partition(a_list, l, r)
    if p_idx == k-1:
        return a_list[k-1]
    if k < p_idx:
        return _kth(a_list, l, p_idx-1, k)
    else:
        return _kth(a_list, p_idx+1, r, k)

def partition(a_list, l, r):
    pivot = a_list[(l+r)//2]
    while l < r:
        while a_list[l] < pivot:
            l+=1
        while a_list[r] > pivot:
            r-=1

        if l < r:
            a_list[l], a_list[r] = a_list[r], a_list[l]

        print(a_list)
    return l


if __name__ == '__main__':
    a = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print(kth(a, 3))



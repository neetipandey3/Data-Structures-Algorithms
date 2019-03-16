

def q_sort(a_list, l, r):
    if l < r:
        p_idx = partition(a_list, l, r)

        q_sort(a_list, l, p_idx-1)
        q_sort(a_list, p_idx+1, r)

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
    print("done")
    return l


if __name__ == '__main__':
    a = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    q_sort(a, 0, len(a)-1)
    print(a)


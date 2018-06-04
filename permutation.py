'''
Given a collection of distinct integers, return all possible permutations.

Example:

Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]

'''
class Permutation:

    def permuteRec(self, nums):

        result = []

        def permute(arr, rest):

            if len(rest) == 0:
                result.append(arr)

            for i in range(len(rest)):
                the_arr_so_far = arr[:]   #create a shallow copy
                the_arr_so_far.append(rest[i])
                permute(the_arr_so_far, rest[:i] + rest[i+1:])

        permute([], nums)
        return result




def main():
    permutation = Permutation()
    print(permutation.permuteRec([1, 2, 3]))
    #print(permutation.permuteRec("abc"))
if __name__ == "__main__":
    main()
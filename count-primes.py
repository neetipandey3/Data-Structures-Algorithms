class Prime:
    def count_primes(self, n):
        """
        :type n: int
        :rtype: int


        Count the number of prime numbers less than a non-negative number, n.

        Example:

        Input: 10
        Output: 4
        Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.


        Solution:
        Sieve of Eratosthenes
        https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
        """

        if n < 3:
            return 0

        result = [True for _ in range(n)]

        result[0] = result[1] = False

        for i in range(2, n // 2 + 1):
            if result[i]:
                result[i * i:n:i] = [False] * len(result[i * i:n:i])

        return sum(result)


def main():
    p = Prime()
    print(p.count_primes(30))

if __name__ == "__main__":
    main()
class Strings:
    def reverse(self, x):
        """
        :type x: string
        :rtype: string
        """
        return x[::-1]

    def reverse_int(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 0:
            rev = int("-"+str(abs(x))[::-1])
        else:
            rev = int(str(x)[::-1])
        if rev < -2**31 or rev > 2**31 - 1:
            rev = 0
        return rev

def main():
    s = Strings()

    print(s.reverse_int(-123))
if __name__ == "__main__":
    main()


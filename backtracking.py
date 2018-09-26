class Backtracking:
    def letter_combinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """

        '''Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.

        A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.
        
        Example:
        
        Input: "23"
        Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].'''

        if not digits:
            return []
        result = []

        ltr_dict = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}

        def combination(comb, idx):
            if idx == len(digits):
                result.append(comb)
            else:
                for c in ltr_dict[digits[idx]]:
                    combination(comb + c, idx + 1)

        combination("", 0)

        return result


def main():
    b = Backtracking()
    print(b.letter_combinations("23"))




if __name__ == "__main__":
    main()

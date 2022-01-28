class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        n = 2*numRows-2     # nums / 1 cycle (반복 한 번의 횟 수)
        array = []
        for _ in range(numRows):
            array.append([])
        for i in range(len(s)):
            rem = i % n     #  remainder
            if rem <= n/2:
                array[rem].append(s[i])
            else:
                array[n-rem].append(s[i])
        st = ""
        for i in range(numRows):
            st += "".join(array[i])
        return st
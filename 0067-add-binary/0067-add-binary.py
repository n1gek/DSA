class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i, j = len(a) - 1, len(b) - 1
        carry = 0
        res = []

        while i >= 0 or j >= 0 or carry:
            da = int(a[i]) if i >= 0 else 0
            db = int(b[j]) if j >= 0 else 0
            total = da + db + carry
            res.append(str(total & 1))   # total % 2
            carry = total >> 1          # total // 2
            i -= 1
            j -= 1

        return ''.join(reversed(res))

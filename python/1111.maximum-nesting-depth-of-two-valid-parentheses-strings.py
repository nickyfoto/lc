class Solution:
    # def maxDepthAfterSplit(self, seq: str) -> List[int]:
    def maxDepthAfterSplit(self, seq):
        def depth(seq):
            n = len(seq)
            if not seq:
                return 0
            stack = []
            A = ""
            B = ""
            for i in range(n):
                if seq[i] == '(':
                    stack.append(seq[i])
                if seq[i] == ')':
                    A += stack.pop()
                    A += ')'
                if not stack:
                    # print(A)
                    if seq[i+1:]:
                        A = seq[:i+1]
                        B = seq[i+1:]
                    break
            print('A=', A, 'B=', B)     
            if not B:
                A = A[:-2]
                return 1 + depth(A)
            return max(depth(A), depth(B))
                    # if i == n - 1:
                    #     print('type A')
                    # else:
                    #     print('type AB')
                    #     break
        return depth(seq)


s = Solution()


seq = "(((())))"
# seq = "(())"
print(s.maxDepthAfterSplit(seq))
# seq = ""
# print(s.maxDepthAfterSplit(seq) == 0)
# seq = "()"
# print(s.maxDepthAfterSplit(seq) == 1)
# seq = "()()"
# print(s.maxDepthAfterSplit(seq) == 1)
# seq = "()(()())"
# print(s.maxDepthAfterSplit(seq) == 2)


# seq = "(())"
# print(s.maxDepthAfterSplit(seq) == 2)


# seq = "(())()"
# print(s.maxDepthAfterSplit(seq) == 2)

# seq = "(()())"
# print(s.maxDepthAfterSplit(seq) == 2)
# print(s.maxDepthAfterSplit(seq))
# print(max(s.maxDepthAfterSplit('()'), s.maxDepthAfterSplit('()()')))

# seq = "()(())()"
# print(s.maxDepthAfterSplit(seq))
# print(max(s.maxDepthAfterSplit('()()'), s.maxDepthAfterSplit('()()')))


# AB or (A)
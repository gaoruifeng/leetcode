class Solution:
    def simplifyPath(self, path: str) -> str:
        arr, my_stack = path.split('/'), []
        for d in arr:
            if d == '..':
                if my_stack: del my_stack[-1]
            elif d != '' and d != '.':
                my_stack.append(d)
        return '/' + '/'.join(my_stack)

if __name__ == '__main__':
    s = Solution()
    print(s.simplifyPath("/home/../../"))

# https://leetcode.com/problems/simplify-path/description/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days&status=TO_DO&difficulty=MEDIUM&role=backend



class Solution:
    def simplifyPath(self, path: str) -> str:
        parts = []

        i = 0
        part = ''
        while i < len(path):
            # move past any '/' characters
            if path[i] == '/':
                if part: # if we are hitting a forward slash right after a valid part, save the part and clear
                    if part == '..':
                        if len(parts):
                            parts.pop()
                    elif part != '.':
                        parts.append(part)

                    part = ''
            else:
                part += path[i]

            i += 1

        if part:
            if part == '..':
                if len(parts):
                    parts.pop()
            elif part != '.':
                parts.append(part)

        return "/" + "/".join(parts)


s = Solution()

assert(s.simplifyPath("/a//b////c/d//././/..") == "/a/b/c")
#assert(s.simplifyPath("/home/") == "/home")
#assert(s.simplifyPath("/home//foo/") == "/home/foo")
#assert(s.simplifyPath("/home/user/Documents/../Pictures") == "/home/user/Pictures")
assert(s.simplifyPath("/../") == "/")
assert(s.simplifyPath("/.../a/../b/c/../d/./") == "/.../b/d")


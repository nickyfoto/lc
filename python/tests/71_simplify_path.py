#
# @lc app=leetcode id=71 lang=python3
#
# [71] Simplify Path
#
# https://leetcode.com/problems/simplify-path/description/
#
# algorithms
# Medium (30.89%)
# Likes:    607
# Dislikes: 1539
# Total Accepted:    184K
# Total Submissions: 595.3K
# Testcase Example:  '"/home/"'
#
# Given an absolute path for a file (Unix-style), simplify it. Or in other
# words, convert it to the canonical path.
# 
# In a UNIX-style file system, a period . refers to the current directory.
# Furthermore, a double period .. moves the directory up a level. For more
# information, see: Absolute path vs relative path in Linux/Unix
# 
# Note that the returned canonical path must always begin with a slash /, and
# there must be only a single slash / between two directory names. The last
# directory name (if it exists) must not end with a trailing /. Also, the
# canonical path must be the shortest string representing the absolute
# path.
# 
# 
# 
# Example 1:
# 
# 
# Input: "/home/"
# Output: "/home"
# Explanation: Note that there is no trailing slash after the last directory
# name.
# 
# 
# Example 2:
# 
# 
# Input: "/../"
# Output: "/"
# Explanation: Going one level up from the root directory is a no-op, as the
# root level is the highest level you can go.
# 
# 
# Example 3:
# 
# 
# Input: "/home//foo/"
# Output: "/home/foo"
# Explanation: In the canonical path, multiple consecutive slashes are replaced
# by a single one.
# 
# 
# Example 4:
# 
# 
# Input: "/a/./b/../../c/"
# Output: "/c"
# 
# 
# Example 5:
# 
# 
# Input: "/a/../../b/../c//.//"
# Output: "/c"
# 
# 
# Example 6:
# 
# 
# Input: "/a//b////c/d//././/.."
# Output: "/a/b/c"
# 
# 
#

# @lc code=start
class Solution:
    # def simplifyPath(self, path: str) -> str:
    def simplifyPath(self, path):
        """
        stacks represent folder hierarchy
        find res will be '/' or '/' + '/'.join(stacks)
        """
        
        stack = []
        i = 0
        # print(len(path))
        while i < len(path) - 1:
            # print('here')
            
            if path[i] == '/':
                j = i + 1
                folder_name = None
                while j < len(path) - 1 and path[j] != '/':
                    j += 1
                if j == len(path) - 1 and path[j] != '/':
                    folder_name = path[i+1:j+1]
                else:
                    folder_name = path[i+1:j]
                # print(i, j, folder_name)
                if folder_name:
                    if folder_name == '..':
                        if stack:
                            stack.pop()
                    elif folder_name == '.':
                        pass
                    else:
                        stack.append(folder_name)
            i = j
        # print(stack)
        return '/' + "/".join(stack)
                
# @lc code=end

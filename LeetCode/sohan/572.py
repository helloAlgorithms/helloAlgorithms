class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def serialize(node, tree_str):
            if node is None:
                tree_str.append('#')
                return

            tree_str.append("^")
            tree_str.append(str(node.val))
            serialize(node.left, tree_str)
            serialize(node.right, tree_str)

        def kmp(needle, haystack):
            m = len(needle)
            n = len(haystack)

            if n < m:
                return False

            lps = [0]*m
            prev = 0
            i = 1

            while i < m:
                if needle[i] == needle[prev]:
                    prev += 1
                    lps[i] = prev
                    i += 1
                else:
                    if prev == 0:
                        lps[i] = 0
                        i += 1
                    else:
                        prev = lps[prev-1]

            haystack_pointer = 0
            needle_pointer = 0

            while haystack_pointer < n:
                if haystack[haystack_pointer] == needle[needle_pointer]:
                    needle_pointer += 1
                    haystack_pointer += 1
                    if needle_pointer == m:
                        return True
                else:
                    if needle_pointer == 0:
                        haystack_pointer += 1
                    else:
                        needle_pointer = lps[needle_pointer-1]
            
            return False

        root_list = []
        serialize(root, root_list)
        r = "".join(root_list)

        subroot_list = []
        serialize(subRoot, subroot_list)
        s = "".join(subroot_list)

        return kmp(s, r)

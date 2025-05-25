from typing import List
import random

# class TreeNode:
#     start = None
#     end = None
#     left = None
#     right = None
#
#     def __init__(self, start, end):
#         self.start = start
#         self.end = end
#         self.left = None
#         self.right = None



class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 0:
            return []

        self.quick_sort(intervals, 0, len(intervals) - 1)

        output = [intervals[0]]
        for elem in intervals[1:]:
            end_idx = output[-1][1]

            if elem[0] <= end_idx:
                output[-1][1] = max(elem[1], end_idx)
            else:
                output.append(elem)
        return output


    def quick_sort(self, intervals, start, end):
        if start >= end:
            return

        def partition(left, right):
            ran_idx = random.randint(left, right)
            pivot = intervals[ran_idx]
            intervals[right], intervals[ran_idx] = intervals[ran_idx], intervals[right]

            l, r = left - 1, left
            while r < right:
                if intervals[r][0] < pivot[0]:
                    l += 1
                    intervals[l], intervals[r] = intervals[r], intervals[l]
                r += 1

            l += 1
            intervals[l], intervals[right] = intervals[right], intervals[l]
            return l
        pivot_idx = partition(start, end)
        self.quick_sort(intervals, start, pivot_idx - 1)
        self.quick_sort(intervals, pivot_idx + 1, end)


# for _ in range(10):
#     a = [[1,3],[2,6],[8,10],[15,18]]
#     Solution().quick_sort(a, 0, 3)
#     print(a)

a = Solution().merge([[15,18],[1,3],[8,10],[2,6]])
print(a)

# if len(intervals) == 0:
#     return []
#
# root = None
# res = []
#
#
# def create_bst(node):
#     curr_node = root
#     while curr_node:
#         prev = None
#         if curr_node.start > node.end:
#             curr_node = curr_node.left
#             prev = curr_node
#         elif curr_node.end < node.start:
#             curr_node = curr_node.right
#             prev = curr_node
#         else:
#
#             curr_node.start = min(node.start, curr_node.start)
#             curr_node.end = max(node.end, curr_node.end)
#
#
# def in_order_trav(node):
#     if node is not None:
#         in_order_trav(node.left)
#         res.append([node.start, node.end])
#         in_order_trav(node.right)
#
#
# root = TreeNode(intervals[0][0], intervals[0][1])
# create_bst(root)
#
# for idx in range(1, len(intervals)):
#     node = TreeNode(intervals[idx][0], intervals[idx][1])
#     create_bst(node)
#
# in_order_trav(root)
# return res
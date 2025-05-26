from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        adjacency_map = {i:[] for i in range(numCourses)}
        for course, pre_req in prerequisites:
            adjacency_map[course].append(pre_req)
        res = []
        visited = set()
        def dfs(course):
            if course in visited:
                return False
            course_pre_req = adjacency_map[course]
            if len(course_pre_req) == 0:
                if course not in res:
                    res.append(course)
                return True
            visited.add(course)
            for pre_req in course_pre_req:
                can_complete = dfs(pre_req)
                # if can_complete:
                #     if course not in res:
                #         res.append(course)
                if not can_complete:
                    return False
            adjacency_map[course] = []
            visited.remove(course)
            if course not in res:
                res.append(course)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return []
        return res


a = Solution().findOrder(6, [[2,3],[1,2],[0,1],[0,4],[4,5],[5,1]])
print(a)




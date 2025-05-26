from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjacency_map = {}
        for item in prerequisites:
            course = item[0]
            pre_req = item[1]
            course_pre_req = adjacency_map.get(course, [])
            course_pre_req.append(pre_req)
            adjacency_map[course] = course_pre_req

        visited = set()

        def dfs(course):
            if course not in adjacency_map:
                return True
            if course in visited:
                return False
            course_pre_req = adjacency_map[course]
            if len(course_pre_req) == 0:
                return True
            completable_pre_req = []
            visited.add(course)
            for pre_req in course_pre_req:
                can_complete = dfs(pre_req)
                if not can_complete:
                    return False
            visited.remove(course)
            adjacency_map[course] = []
            return True

        for crs, _ in prerequisites:
            if not dfs(crs):
                return False
        return True


a = Solution().canFinish(20, [[1,4],[2,4],[3,1],[3,2]])
print(a)

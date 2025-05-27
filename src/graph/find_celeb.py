# The knows API is already defined for you.
# return a bool, whether a knows b
def knows(a: int, b: int) -> bool:
    graph = [[1,0],[0,1]]
    return graph[a][b] == 1

class Solution:
    def findCelebrity(self, N: int) -> int:
        # only celeb candifate is `celeb`
        # A --> B means A can't be celeb but B can
        # A ---X---> B means A can be a celeb but B cant

        celeb = 0
        for i in range(N):
            if knows(celeb, i):
                celeb = i


        for i in range(N):
            if i != celeb:
                if not knows(i, celeb) or knows(celeb, i):
                    return -1
        return celeb



a = Solution().findCelebrity(2)
print(a)





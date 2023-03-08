from typing import List
from collections import defaultdict

class Solution:
    """
    time: pending
    space: pending
    """
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # O(n) time, O(n) space
        def dfs(graph, courses, ans, curr):
            if courses[curr] != 0:
                return ans
            ans.append(curr)
            courses[curr] = -1
            if curr in graph:
                for i in graph[curr]:
                    courses[i] -= 1
                    ans = dfs(graph, courses, ans, i)
            return ans
        
        graph = defaultdict(list)
        courses = [0] * numCourses  # O(n) space
        ans = []

        # O(n^2) time(or O(E)) , O(n^2) space
        for i in prerequisites:
            graph[i[1]].append(i[0])
            courses[i[0]] += 1

        # O(n)
        for i in range(numCourses):  
            ans = dfs(graph, courses, ans, i)
        return ans if len(ans) == numCourses else []
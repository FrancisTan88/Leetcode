from collections import defaultdict
from typing import List
class Solution:
    """
    method: Topological Sort - DFS(same as CourseSchedule||)
                Note: the complexity is already the best, but the constant and the operation can be improved.
    time: O(V+E)
    space: O(V+E)
    """
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        def dfs(hashmap, count, curr, ans):
            if count[curr] != 0:
                return ans
            ans.append(curr)
            count[curr] = -1
            if len(ans) == numCourses:
                return ans
            for i in hashmap[curr]:
                count[i] -= 1
                ans = dfs(hashmap, count, i, ans)
                if len(ans) == numCourses:
                    return ans
            return ans
        hashmap = defaultdict(list)
        count = [0] * numCourses
        ans = []
        for curr, pre in prerequisites:
            hashmap[pre].append(curr)
            count[curr] += 1
        for i in range(numCourses):
            ans = dfs(hashmap, count, i, ans)
        return True if len(ans) == numCourses else False
    

    """
    method: Check cycles - DFS(best solution)
    time: O(V+E)
    space: O(V+E)
    """
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        def dfs(adj_lst, visited, curr):
            if visited[curr] == -1:
                return False
            if visited[curr] == 1:
                return True
            visited[curr] = -1
            for i in adj_lst[curr]:
                if not dfs(adj_lst, visited, i):
                    return False
            visited[curr] = 1
            return True
        adj_lst = defaultdict(list)
        visited = [0] * numCourses
        for curr, pre in prerequisites:
            adj_lst[pre].append(curr)
        for i in range(numCourses):
            if not dfs(adj_lst, visited, i):
                return False
        return True
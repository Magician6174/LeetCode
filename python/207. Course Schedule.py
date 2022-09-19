class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        from collections import defaultdict
        
        adj_list = defaultdict(list)
        indegree = {}
        for dest,src in prerequisites:
            adj_list[src].append(dest)
            indegree[dest] = indegree.get(dest,0) + 1
            
        queue = [k for k in range(numCourses) if k not in indegree]
        
        ans = []
        
        while queue:
            
            vertex = queue.pop(0)
            ans.append(vertex)
            
            if vertex in adj_list:
                for neighbor in adj_list[vertex]:
                    indegree[neighbor] -= 1

                    if indegree[neighbor] == 0:
                        queue.append(neighbor)

        return len(ans) == numCourses

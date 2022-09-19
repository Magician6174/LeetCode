class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
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

        return ans if len(ans) == numCourses else []
    
    
    
    
    
    
    
    
    
    
    

"""--------------------------------DFS Solution Topological sort----------------------------"""
# class Solution:
    
#     WHITE = 1
#     GRAY = 2
#     BLACK = 3
    
#     def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
    
#         from collections import defaultdict
        
#         adj_list = defaultdict(list)
        
#         for dest,src in prerequisites:
#             adj_list[src].append(dest)
            
#         topological_sorted_order = []
#         self.is_possible = True
        
#         color = {k: Solution.WHITE for k in range(numCourses)}
#         def dfs(node):
            
#             if not self.is_possible:
#                 return
            
#             color[node] = Solution.GRAY
            
#             if node in adj_list:
#                 for neighbor in adj_list[node]:
#                     if color[neighbor] == Solution.WHITE:
#                         dfs(neighbor)
#                     elif color[neighbor] == Solution.GRAY:
#                         self.is_possible = False
            
#             color[node] = Solution.BLACK
#             topological_sorted_order.append(node)
            
#         for vertex in range(numCourses):
#             if color[vertex] == Solution.WHITE:
#                 dfs(vertex)
        
#         return topological_sorted_order[::-1] if self.is_possible else []
            
        

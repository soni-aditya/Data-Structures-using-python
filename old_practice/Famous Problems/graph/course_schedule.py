'''
There are a total of numCourses courses you have to take, labeled from 0 to numCourses -1
Some courses have pre-requisets, for ex. to take course 0 you have to take course 1 which is a pair [0,1]

Given  the total number of courses, and a list of prerequisit pairs, is it possible for you to finish all courses?

Input: numCourses: 2 and prerequisits = [[1,0]] 
Output: True

Input: numCourses: 2 and prerequisits = [[1,0]] 
Output: True

Input: numCourses: 2 and prerequisits = [[1,0],[0,1]] 
Output: False (because its a deadlock)
'''

# we'll do it through a DFS

class Solution:
    def canFinish(self, numCourses: int, prerequisits: list[list[int]])->bool:
        # map each course to prereq list
        preMap = {i:[] for i in range(numCourses)}

        for course, pre in prerequisits:
            preMap[course].append(pre)

        visitSet = set()

        def DFS(course):
            # if we are visiting a course twice, ie. there's a loop
            if course in visitSet:
                return False
            # if there's no prerequisit of a course
            if preMap[course] ==[]:
                return True
            
            visitSet.add(course)
            for pre in preMap[course]:
                # if there's any course in the prerequisits for which we get a loop, return False
                if not DFS(pre):
                    return False
            visitSet.remove(course)
            # since till now we know that this course can be visited without a loop, lets put its prerequisits as [] to avoid recurssion whenever it appears in future calls
            preMap[course] = []
            return True
        
        for course, _ in preMap.items():
            if not DFS(course): return False
        
        return True
    

sol = Solution()
print(sol.canFinish(2,[[1,0],[0,1]]))
print(sol.canFinish(2,[[1,0]]))
'''
There are a total of n course you have to take labelled from 0 to n-1

Some courses may have prerequisits, for ex. if prerequisits[i] = [a,b] this means that you must take course b before course a

Given a total number of courses numCourses and list of prerequisit pairs, return the ordering of courses you should take to finish all courses

if there are many valid anssers, return any of them. If there's no possible answer, return empty array

Input: numCourses: 2 and prerequisits = [[1,0]] 
Output: [0,1]

Input: numCourses: 2 and prerequisits = [[1,0],[0,1]] 
Output: [] (because its a deadlock)
'''

class Solution:
    def canFinish(self, numCourses: int, prerequisits: list[list[int]])->bool:
        # map each course to prereq list
        preMap = {i:[] for i in range(numCourses)}

        for course, pre in prerequisits:
            preMap[course].append(pre)

        '''
        A course has 3 possible states:
        1. visited - course has been added to output
        2. visiting - course hasn't been added to output, but added to cycle
        3. unvisited - course not added to output or cycle
        '''
        course_order = set()
        visit, cycle = set(), set()

        def DFS(course):
            # if course is already inside a cycle, ie. there's a closed loop
            if course in cycle:
                return False
            # if course is already visited
            if course in visit:
                return True
            
            # add it to cycle, so that if we ever see this course again, we'll know
            cycle.add(course)

            for prereq in preMap[course]:
                if not DFS(prereq): return False # cycle detected in one of the prerequisits
            
            cycle.remove(course)
            visit.add(course)
            course_order.add(course)

            return True

        
        for course, _ in preMap.items():
            if not DFS(course): return []
        
        return list(course_order)
    

sol = Solution()
print(sol.canFinish(2,[[1,0],[0,1]]))
print(sol.canFinish(2,[[1,0]]))
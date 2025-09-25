#im sure theres a better solution here with im guessing a min heap? but this beats 95% of python submissions so im happy with it

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        #dont rly need to take sqrt. just from the sum we will know whats closer

        #min heap? heapify is log(n), but at the same time its nlog(n) because you have to do it for every point 

        #same then to just build the array, sort in nlog(n) time and then return kth value 
        distances = [] 
        for point in points:
            dist = point[0]**2 + point[1]**2
            distances.append((dist, point))

        distances = sorted(distances)    
        res = []  
        for i in range(k):
            res.append(distances[i][1])
        return res

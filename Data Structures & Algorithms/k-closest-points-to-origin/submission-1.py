class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distance = points[1][0]
        distances = []
        for i in range(len(points)):
            x = points[i][0]
            y = points[i][1]
            distance = (x**2)+ (y**2)
            distances.append([distance,points[i]])
        distances.sort()
        results = []
        for i in range(k):
            results.append(distances[i][1])
        return results


        
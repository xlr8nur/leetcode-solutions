'''
Question;

You are given an 2-D array points where points[i] = [xi, yi] represents the coordinates of a point on an X-Y axis plane. You are also given an integer k.
Return the k closest points to the origin (0, 0).
The distance between two points is defined as the Euclidean distance (sqrt((x1 - x2)^2 + (y1 - y2)^2)).
You may return the answer in any order.
'''

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        for x, y in points:
            dist = (x ** 2) + (y ** 2)
            minHeap.append((dist, x, y))
        
        heapq.heapify(minHeap)
        res = []
        for _ in range(k):
            _, x, y = heapq.heappop(minHeap)
            res.append((x, y))
        return res

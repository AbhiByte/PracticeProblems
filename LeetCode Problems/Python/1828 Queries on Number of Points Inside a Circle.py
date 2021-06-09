## Going for o(n) complexity
import math
def countPoints(points, queries):
    ans = []
    ansIndexCounter = 0
    for i in range(len(queries)):
        totalPointsInCircle = 0
        radius = queries[i][2]

        for x in range(len(points)):
            distance = math.sqrt((points[x][0] - queries[i][0])*(points[x][0] - queries[i][0]) + (points[x][1] - queries[i][1])*(points[x][1] - queries[i][1]))
            if distance <= radius:
                totalPointsInCircle += 1

        ans.append(totalPointsInCircle)
    return ans



points = [[1,3],[3,3],[5,3],[2,2]]
queries = [[2,3,1],[4,3,1],[1,1,2]]
print(countPoints(points, queries))

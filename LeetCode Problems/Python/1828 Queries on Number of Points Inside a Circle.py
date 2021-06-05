
def countPoints(points, queries):
    radii = []
    ans = []
    sum = 0
    for i in range(len(queries)):
        for j in range(len(queries[i])):
            if j == 0 and j+1 == 1:

    for x in range(len(points)):
        for y in range(len(points[x])):
            if y == 0 and y+1 == 1:


            if j == 2:
                radii.append(queries[i][j])



points = [[1,3],[3,3],[5,3],[2,2]]
queries = [[2,3,1],[4,3,1],[1,1,2]]
print(countPoints(points, queries))

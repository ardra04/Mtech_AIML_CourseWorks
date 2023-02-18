#Start from the leftmost point (/ point with min x coord val) and keep wrapping points in counterclockwise direction. 
# next point is q if for any other point r, we have “orientation(p, q, r) = counterclockwise.

def jarvis(points):
    n = len(points)
    start = points[0]    # starting point =  leftmost point
    for i in range(1, n):
        if points[i][0] < start[0]:
            start = points[i]
    current = start                #  current point = starting point
    convex_hull = [start]
    while True:                        # Repeat until the current point is the starting point
        next_point = points[0]          #  next point =  first point
        for i in range(1, n):
            angle = angle_between(current, next_point, points[i])  # Find point that make smallest <le with the current point
            if angle < 0 or (angle == 0 and distance(current, points[i]) > distance(current, next_point)):
                next_point = points[i]
        current = next_point
        if current == start:            # If the next point is the starting point, the convex hull is complete
            break
        convex_hull.append(current)
    return convex_hull

def angle_between(p1, p2, p3):
    angle = (p3[1] - p1[1]) * (p2[0] - p1[0]) - (p2[1] - p1[1]) * (p3[0] - p1[0])  #Return <le b/w line p1-p2 and line p1-p3
    return angle

def distance(p1, p2):
    return ((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2) ** 0.5    # Returns the Euclidean distance between two points

points = [[2, 3], [4, 4], [5, 2], [2, 1], [1, 5]]
convex_hull = jarvis(points)
print(convex_hull)


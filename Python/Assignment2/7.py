'''Given N points on a circle, centered at the origin, design an algorithm that determines whether there are two points that are antipodal, i.e., the line connecting the two points goes through the origin. Your algorithm should run in time proportional to N logN .'''

# import math

# def checkAntipodal(points):
#     # Step 1: Compute angles for all points
#     angles = sorted(math.atan2(y, x) for x, y in points)  # O(N log N) sorting

#     # Step 2: Check if any two angles differ by exactly π (180 degrees)
#     n = len(angles)
#     for i in range(n):
#         for j in range(i + 1, n):
#             if math.isclose(abs(angles[j] - angles[i]), math.pi, rel_tol=1e-9):
#                 return True  # Found antipodal points
    
#     return False  # No antipodal points found

# points = [(1, 0), (0, 1), (-1, 0), (0, -1)]
# if checkAntipodal(points):
#     print("Antipodal points exist.")
# else:
#     print("Antipodal points do not exist.")



# def quadrant(x, y):
#     """Determine which quadrant the point (x, y) is in."""
#     if x >= 0 and y >= 0:  # Quadrant 1
#         return 1
#     if x < 0 and y >= 0:   # Quadrant 2
#         return 2
#     if x < 0 and y < 0:    # Quadrant 3
#         return 3
#     return 4               # Quadrant 4

# def custom_sort(point):
#     """Sorting function to sort points by angle without using atan2."""
#     x, y = point
#     q = quadrant(x, y)  # Get the quadrant
#     slope = y * 1.0 / x if x != 0 else float('inf')  # Compute slope manually
#     return (q, slope)  # Sort by quadrant first, then slope

# def checkAntipodal(points):
#     """Check if there are two antipodal points on the circle."""
#     # Step 1: Sort points based on quadrant and slope
#     points.sort(key=custom_sort)  # O(N log N) sorting

#     # Step 2: Check if any two points are antipodal
#     n = len(points)
#     for i in range(n):
#         x1, y1 = points[i]
#         for j in range(i + 1, n):  # Look ahead in sorted order
#             x2, y2 = points[j]
#             if x1 == -x2 and y1 == -y2:
#                 return True  # Found an antipodal pair

#     return False  # No antipodal points found

# points = [(1, 0), (0, 1), (-1, 0), (0, -1)]
# if checkAntipodal(points):
#     print("Antipodal points exist.")
# else:
#     print("Antipodal points do not exist.")



print('''Name: Sidhanta Barik, RegNo: 2241002049
-----------------------------------------''')
def quadrant(x, y):
    if x >= 0 and y >= 0:
        return 1
    if x < 0 and y >= 0:
        return 2
    if x < 0 and y < 0:
        return 3
    return 4

def custom_sort(point):
    x, y = point
    q = quadrant(x, y)
    if x != 0:
        slope = y * 1.0 / x
    else:
        slope = float('inf')    
    return (q, slope)

def checkAntipodal(points):
    points.sort(key=custom_sort)
    n = len(points)
    for i in range(n):
        x1, y1 = points[i]
        for j in range(i + 1, n):
            x2, y2 = points[j]
            if x1 == -x2 and y1 == -y2:
                return True
    return False

points = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1)]
if checkAntipodal(points):
    print("Antipodal points exist.")
else:
    print("Antipodal points do not exist.")

# Name: Sidhanta Barik, RegNo: 2241002049
# -----------------------------------------
# Antipodal points exist.
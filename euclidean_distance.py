import math

# List of points in 2D space
points = [(1, 2), (3, 4), (5, 6), (7, 8)]

# Function to calculate Euclidean distance between two points
def euclideanDistance(point1, point2):
    return math.sqrt((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2)

# Calculate distances between each pair of points
distances = []
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        distance = euclideanDistance(points[i], points[j])
        distances.append(distance)

# Find the minimum distance
min_distance = min(distances)

print("The minimum Euclidean distance is:", min_distance)

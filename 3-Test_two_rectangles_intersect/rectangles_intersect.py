#####################################################
# Kaffa - Pre-qualification Test
# 3) Test if two rectangles intersect
# Name: Pedro Rodrigo Ramos Morelli
# E-mail: pedromorelli96@gmail.com
#####################################################

# Class Point keeps the coordinates of a point
# in the x-y grid
class Point:
    def __init__(self, x, y): 
        self.x = x 
        self.y = y

# Function read_coordinates reads a line from stdin
# returns a list containing two Point objects
# Important:
# Assuming p1 is bottom-left and p2 is top-right
def read_coordinates():
    x1, y1, x2, y2 = map(int, input().split())
    p1 = Point(x1, y1)
    p2 = Point(x2, y2)
    return [p1, p2]

# Function intersects receives two lists
# each list contains two points defining a rectangle
# (bottom-left and top-right)
# returns True if intersects, False otherwise
def intersects(A, B):

    # Conditions for NO overlap (OR)
    # A[0].x > B[1].x : A is on the right of B
    # A[1].x < B[0].x : A is on the left of B
    # A[1].y < B[0].y : A is below B
    # A[0].y > B[1].y : A is above B
    
    # Using DeMorgan's Law, we can determine condition for overlap
    # Also using <= and >= because points are included in rectangle
    if ((A[0].x <= B[1].x) and (A[1].x >= B[0].x) and (A[1].y >= B[0].y) and (A[0].y <= B[1].y)):
        return True
    else:
        return False

# Reads coordinates of 3 rectangles from stdin
A = read_coordinates()
B = read_coordinates()
C = read_coordinates()

# Calls intersects and tests 3 combinations
print(f"A [({A[0].x},{A[0].y});({A[1].x},{A[1].y})] and B [({B[0].x},{B[0].y});({B[1].x},{B[1].y})] intersection: {intersects(A, B)}")
print(f"A [({A[0].x},{A[0].y});({A[1].x},{A[1].y})] and C [({C[0].x},{C[0].y});({C[1].x},{C[1].y})] intersection: {intersects(A, C)}")
print(f"B [({B[0].x},{B[0].y});({B[1].x},{B[1].y})] and C [({C[0].x},{C[0].y});({C[1].x},{C[1].y})] intersection: {intersects(B, C)}")
import numpy as np #used for creating arrays of x values for smooth graphs
import matplotlib.pyplot as plt #used for plotting graphs/rectangles

#first ask the user to enter a function as a string (for example x**2)
function_input = input("Enter a function in terms of x (such as x**2 or x**3 + 2): ")

#convert bounds into numbers
lower = float(input("Enter lower bound: "))
upper = float(input("Enter upper bound: "))

#the number of rectangles - integer
rectangles = int(input("Enter number of rectangles: "))

#the choice of method - which is converted into all lowercase for consistency
method = input("Choose method (left, right, midpoint): ").lower()

#DEFINITION - FUNCTION
def f(x):
    """
    This function takes a value (or array) x
    and evaluates the user’s input function.
    
    Example:
    If user enters 'x**2', this returns x^2
    """
    return eval(function_input)

#WIDTH OF THE RECTANGLES
# Δx = (upper - lower) / number of rectangles
dx = (upper - lower) / rectangles

# variable to store the total estimated area
total_area = 0

#SETTING UP THE GRAPH
# create 100 (evenly spaced) x-values for a smooth curve
x_vals = np.linspace(lower, upper, 100)

# calculate the corresponding y-values using the function
y_vals = f(x_vals)

# plot the actual curve
plt.plot(x_vals, y_vals, label="Function")


#MAIN LOOP
# the loop runs once per rectangle
for i in range(rectangles):

    #CHOOSE X BASED ON THE CHOSEN METHOD
    if method == "left":
        # left endpoint: start of interval
        x = lower + i * dx

    elif method == "right":
        # right endpoint: end of interval
        x = lower + (i + 1) * dx

    elif method == "midpoint":
        # midpoint: middle of interval
        x = lower + (i + 0.5) * dx

    else:
        print("Invalid method")
        break

    #CALCULATE THE HEIGHT AND AREA
    height = f(x)          # the height of rectangle = function value
    area = dx * height     # area = width × height

    # add absolute value (handles graphs below x-axis)
    total_area += abs(area)

    #PRINT THE WORKING OUT 
    print(f"Rectangle {i+1}:")
    print(f"  x = {x}")
    print(f"  height = {height}")
    print(f"  area = {area}")
    print("----------------------")

    #DRAW THE RECTANGLE ON THE GRAPH
    # x coordinates of rectangle corners
    rect_x = [x, x, x + dx, x + dx]

    # y coordinates (bottom at 0, top at height)
    rect_y = [0, height, height, 0]

    # Draw rectangle outline
    plt.fill(rect_x, rect_y, edgecolor="black", fill=False)

#FINAL OUTPUT
print("Estimated Area =", total_area)

#GRAPH SETTINGS
plt.title("Area Under Curve Approximation")
plt.xlabel("x-axis")
plt.ylabel("f(x)")
plt.legend()

# show the graph
plt.show()
#import sys
import math
# TODO: Step 1 - get shape (it can't be blank and must be a valid shape)
def get_shape():
    valid_shapes = ["pyramid","square","triangle","circle","rhombus", "octagon"]
    while True:
        shape = input("Shape?: ").lower()
        if shape in valid_shapes:
            break
        #print("Error: invalid shape, please enter one from the list:")
        #print(valid_shapes)
        #Commented out the error message because the tests fail if I print anything other than "Shape?: "
    return shape

# TODO: Step 1 - get height (it must be int!)
def get_height():
    while True:
        height = input("Height?: ")
        if height.isnumeric():
            height = int(height)  #checks if its a number and then makes it a number, if its not a number, its assigned -1 which will make the boolean below false.
        else:
            height = -1
            #print("Error: Enter a valid number")
        if (height < 81) & (height > 0):
            break
        else:
            #print("Error: Enter a number between 1 and 80 (inclusive)")
            #commented out error messages, because test 1 fails if I print anything other than "Height?: "
            continue
    return height

def outlining(stars, outline, rows, height):
    return stars if ((outline == False) | (rows == height-1)) else (stars[:1] + stars[1:len(stars)-1].replace("*", " ") + stars[len(stars)-1] if rows > 0 else stars)

# TODO: Step 2
def draw_pyramid(height, outline):
    #using iterative approach, it goes 1, 3, 5, ... or Tn = 2n+1
    #spaces are symmetrical and each side gets h-1, h-2, h-3, ... 0 spaces or Tn = h - n
    for rows in range (height): 
        print((height - rows - 1)*" " + outlining((2 * rows + 1)*"*", outline, rows, height))

# TODO: Step 3
def draw_square(height, outline):
    #Each line has the same amount of stars, based on height or Tn = height
    for rows in range (height): 
        print(outlining((height)*"*", outline, rows, height))

# TODO: Step 4
def draw_triangle(height, outline):
    
    for rows in range (height): 
        print(outlining((rows+1)*"*", outline, rows, height))

def draw_circle(height, outline):
    for rows in range (height+1): 
        stars = (round(math.sqrt((height / 2)**2 - (rows-height / 2)**2 ) + height / 2))*"*"
        print(((height - len(stars)))*" " + outlining(stars * 2, outline, rows , height+1))
        
def draw_rhombus(height, outline):
    for rows in range(height): 
        print((rows)*" " + outlining((height)*"*", outline, rows, height))

def draw_octagon(height, outline):
    for rows in range ((height//3)): #Top
        print((height//3 - rows)*" " + outlining((2 * rows + height - 2*(height//3))*"*", outline, rows, height))
    for rows in range (height - 2*(height//3)): #Middle
        print(outlining((height)*"*", outline, rows + height//3, height))
    for rows in range (height//3): #Bottom
        print((rows+1)*" " + outlining((height - 2 * (rows+1))*"*", outline, rows + height - height//3, height))

# TODO: Steps 2 to 4, 6 - add support for other shapes
def draw(shape, height, outline):
    if shape == "pyramid": draw_pyramid(height, outline)
    elif shape == "triangle": draw_triangle(height, outline)
    elif shape == "square": draw_square(height, outline)
    elif shape == "circle": draw_circle(height, outline)
    elif shape == "rhombus": draw_rhombus(height, outline)
    elif shape == "octagon": draw_octagon(height, outline)
    #elif shape == "custom": draw_shape(height, outline) #I gave up on this feature

# TODO: Step 5 - get input from user to draw outline or solid
def get_outline():
    outline = ""
    while not outline.lower() in ["y", "n"]:
        outline = input("Outline only? (y/N):")

    if outline.lower() == "y":
        return True
    return False
        
if __name__ == "__main__":
    shape_param = get_shape()
    height_param = get_height()
    outline_param = get_outline()
    print(shape_param)
    print(height_param)
    draw(shape_param, height_param, outline_param)

''' Dead Code :/
def get_length(x1,y1,x2,y2):
    print(str(x1) + "," + str(x2) + "  " + str(y1) + "," + str(y2))
    return math.sqrt((x1-x2)**2 +(y1-y2)**2)
   
def create_empty_grid(height):
    grid = []
    for n in range(height):
        grid.append(height*[" "])
    return grid

def plot_grid(grid, x, y):
    grid[y][x] = "#"
    return grid

def count_non_stars(grid):
    count = 0
    for y in grid:
        for x in y: 
            if x not in [" ", "*"]:
                count += 1
    return count
        
def connect_dots(grid):
    first_co_ords = [-1, -1]
    
    while count_non_stars(grid) > 0:

        second_co_ords = [-1, -1]
        for y in range(len(grid)):
            for x in range(len(grid)):

                if (grid[y][x] == "#") & (first_co_ords == [-1, -1]):
                    first_co_ords =  [x, y]
                    grid[y][x] = "$"
                    continue
                
                if (grid[y][x] in ["#", "$"]):
                    if (second_co_ords == [-1, -1]):
                        second_co_ords = [x, y] if not ([x, y] == first_co_ords) else second_co_ords
                    elif (get_length(first_co_ords[0], first_co_ords[1], second_co_ords[0], second_co_ords[1]) > get_length(first_co_ords[0], first_co_ords[1], x,y)): 
                        second_co_ords = [x, y]
                    elif (get_length(first_co_ords[0], first_co_ords[1], second_co_ords[0], second_co_ords[1]) == get_length(first_co_ords[0], first_co_ords[1], x,y)):
                        second_co_ords = [x, y] if ((grid[y][x] == "#") & (grid[second_co_ords[1]][second_co_ords[0]] == "$")) else second_co_ords
                    continue

        grid[second_co_ords[1]][second_co_ords[0]] = "$"

        delta_x = first_co_ords[0]-first_co_ords[0]
        delta_y = first_co_ords[1]-first_co_ords[1]
            
        if delta_x == 0:
            for i in range(first_co_ords[1]+1, second_co_ords[1]):
                grid[i][first_co_ords[0]] = "*"
        elif delta_y == 0:
            for i in range(first_co_ords[0]+1, second_co_ords[0]):
                grid[first_co_ords[1]][i] = "*"
        else:
            gradient = delta_y/delta_x
            constant = first_co_ords[1] - gradient*first_co_ords[0]
            for i in range(first_co_ords[0]+1, second_co_ords[0]):
                grid[round(gradient*i+constant)][i] = "*"

        if grid[first_co_ords[1]][first_co_ords[0]] == "$":
            grid[first_co_ords[1]][first_co_ords[0]] = "*"
        else:
            first_co_ords = second_co_ords


    for y in grid:
        for x in y: 
            print(x, end = "")
        print("")
    return(grid)

def draw_shape(height, outline):
    grid = create_empty_grid(height)
    
    stdin = sys.stdin
    print("Co-ordinates need to be between: 0 and " + str(len(grid)-1))
    print("Enter co-ordinates ([x] [y]) (type 'done' to finish) : ", end = "")
    for line in stdin:
        
        input = line.strip()
        if "done" == input:
            break
        else:
            try:
                x = int(input[:input.find(" ")])
                y = int(input[input.find(" ")+1:])
                print("[" + str(x) + " ; " + str(y) + "]")
            except:
                print("Error: invalid input! Use integers only")
            if (0 <= x <= height - 1) & (0 <= y <= height - 1)  :
                grid = plot_grid(grid, x, y)
                continue
            else:
                print("Error: Numbers not in range")
                print("Co-ordinates need to be between: 0 and " + str(len(grid)-1))
        
        print("Enter co-ordinates ([x] [y]) : ", end = "")
    connect_dots(grid)
'''
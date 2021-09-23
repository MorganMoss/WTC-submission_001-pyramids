#import sys
import math
# TODO: Step 1 - get shape (it can't be blank and must be a valid shape)
def get_shape():
    valid_shapes = ["pyramid","square","triangle","circle","rhombus", "octagon"]
    while True:
        shape = input("Shape?: ").strip().lower()
        if shape in valid_shapes:
            break
        #print("Error: invalid shape, please enter one from the list:")
        #print(valid_shapes)
        #Commented out the error message because the tests fail if I print anything other than "Shape?: "
    return shape

# TODO: Step 1 - get height (it must be int!)
def get_height():
    while True:
        height = input("Height?: ").strip()
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
    #This takes a row of stars and hollows it out if outline is true.
    #Code broken up:
    #if (not outline) or (rows == height) or (rows == 0):
        #return stars
    #else:
        #return stars[:1] + stars[1:len(stars)-1].replace("*", " ") + stars[len(stars)-1]
    return stars if ((outline == False) | (rows == height-1) | (rows == 0)) else (stars[:1] + stars[1:len(stars)-1].replace("*", " ") + stars[len(stars)-1])

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

# TODO: Step 6
def draw_circle(height, outline):
    if height == 1:
        print("*")
    elif height == 2:
        print("**\n**")
    else:
        #below code only works for circles of height >= 3
        height -= 1 #to get the circle to work with my outlining tool, I make the for loop be one size bigger, and to reduce it again, I make height 1 less
        for rows in range (height+1): 
            stars = (round(math.sqrt((height / 2)**2 - (rows-height / 2)**2 ) + height / 2))*"*"
            print(((height - len(stars)))*" " + outlining(stars * 2 , outline, rows , height+1))

# TODO: Step 6       
def draw_rhombus(height, outline):
    for rows in range(height): 
        print((rows)*" " + outlining((height)*"*", outline, rows, height))
        
# TODO: Step 6
def draw_octagon(height, outline):
    for rows in range (height//3): #Top
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
    

# TODO: Step 5 - get input from user to draw outline or solid
def get_outline():
    outline = "YEET"
    while not outline in ["y", "n" , ""]:
        outline = input("Outline only? (y/N):").strip().lower()

    if outline == "y":
        return True
    return False
        
if __name__ == "__main__":
    shape_param = get_shape()
    height_param = get_height()
    outline_param = get_outline()
    print(shape_param)
    print(height_param)
    draw(shape_param, height_param, outline_param)


#-----Statement of Authorship----------------------------------------#
#
#  This is an individual assessment item.  By submitting this
#  code I agree that it represents my own work.  I am aware of
#  the University rule that a student must not act in a manner
#  which constitutes academic dishonesty as stated and explained
#  in QUT's Manual of Policies and Procedures, Section C/5.3
#  "Academic Integrity" and Section E/2.1 "Student Code of Conduct".
#
#    Student no: n10163140
#    Student name: Josh Fell
#
#  NB: Files submitted without a completed copy of this statement
#  will not be marked.  All files submitted will be subjected to
#  software plagiarism analysis using the MoSS system
#  (http://theory.stanford.edu/~aiken/moss/).
#
#--------------------------------------------------------------------#



#-----Assignment Description-----------------------------------------#
#
#  CITYSCAPES
#
#  This assignment tests your skills at defining functions, processing
#  data stored in lists and efficiently repeating multiple actions in
#  order to display a complex visual image.  The incomplete
#  Python script below is missing a crucial function, "build_city".
#  You are required to complete this function so that when the
#  program is run it draws a city whose plan is determined by
#  randomly-generated data stored in a list which specifies what
#  style of building to erect on particular sites.  See the
#  instruction sheet accompanying this file for full details.
#
#  Note that this assignment is in two parts, the second of which
#  will be released only just before the final deadline.  This
#  template file will be used for both parts and you will submit
#  your final solution as a single Python 3 file, whether or not you
#  complete both parts of the assignment.
#
#--------------------------------------------------------------------#  



#-----Preamble-------------------------------------------------------#
#
# This section imports necessary functions and defines constant
# values used for creating the drawing canvas.  You should not change
# any of the code in this section.
#

# Import the functions needed to complete this assignment.  You
# should not need to use any other modules for your solution.  In
# particular, your solution must not rely on any non-standard Python
# modules that need to be installed separately, because the markers
# may not have access to such modules.

from turtle import *
from math import *

# Define constant values used in the main program that sets up
# the drawing canvas.  Do not change any of these values.

canvas_height = 700 # pixels
canvas_width = 1100 # pixels
grass_depth = 95 # vertical depth of the "grass", in pixels
half_width = canvas_width // 2 # maximum x coordinate in either direction
grid_font = ('Arial', 10, 'normal') # font for drawing the grid
grid_size = 50 # gradations for the x and y scales shown on the screen
offset = 5 # offset of the x-y coordinates from the screen's edge, in pixels
max_height = canvas_height - grass_depth # maximum positive y coordinate
max_building_height = 575 # city ordinance maximum building height
site_width = 240 # maximum width of a building site

# Define the locations of building sites approved by the
# city council (arranged from back to front)
sites = [['Site 1', [-225, 0]],
         ['Site 2', [25, 0]],
         ['Site 3', [275, 0]],
         ['Site 4', [-375, -25]],
         ['Site 5', [-125, -25]],
         ['Site 6', [125, -25]],
         ['Site 7', [375, -25]],
         ['Site 8', [-275, -50]],
         ['Site 9', [-25, -50]],
         ['Site 10', [225, -50]]]


#
#--------------------------------------------------------------------#



#-----Functions for Creating the Drawing Canvas----------------------#
#
# The functions in this section are called by the main program to
# manage the drawing canvas for your image.  You should not change
# any of the code in this section.
#

# Set up the canvas and draw the background for the overall image.
# By default the drawing grid is displayed - call the function
# with False as the argument to prevent this.
def create_drawing_canvas(show_grid = True):

    # Set up the drawing canvas with coordinate (0, 0) in the
    # "grass" area
    setup(canvas_width, canvas_height)
    setworldcoordinates(-half_width, -grass_depth, half_width, max_height)

    # Draw as fast as possible
    tracer(False)

    # Make the sky blue
    bgcolor('sky blue')

    # Draw the "grass" as a big green rectangle (overlapping the
    # edge of the drawing canvas slightly)
    overlap = 25 # pixels
    penup()
    goto(-(half_width + overlap), -(grass_depth + overlap)) # bottom-left
    fillcolor('pale green')
    begin_fill()
    setheading(90) # face north
    forward(grass_depth + overlap * 2)
    right(90) # face east
    forward(canvas_width + overlap * 2)
    right(90) # face south
    forward(grass_depth + overlap * 2)
    end_fill()

    # Draw a nice warm sun peeking into the image at the top left
    penup()
    goto(-canvas_width // 2, canvas_height - grass_depth)
    pencolor('yellow')
    dot(350)

    # Draw a big fluffy white cloud in the sky
    goto(canvas_width // 3, canvas_height - grass_depth - 100)
    pencolor('white')
    dot(200)
    setheading(200)
    forward(100)
    dot(180)
    setheading(0)
    forward(200)
    dot(160)

    # Optionally draw x coordinates along the bottom of the
    # screen (to aid debugging and marking)
    pencolor('black')
    if show_grid:
        for x_coord in range(-half_width + grid_size, half_width, grid_size):
            goto(x_coord, -grass_depth + offset)
            write('| ' + str(x_coord), font = grid_font)

    # Optionally draw y coordinates on the left-hand edge of
    # the screen (to aid debugging and marking)
    if show_grid:
        for y_coord in range(-grid_size, max_height, grid_size):
            goto(-half_width + offset, y_coord - offset)
            write(y_coord, font = grid_font)
        goto(-half_width + offset, max_building_height - 5)
        write('Maximum allowed building height', font = grid_font)

    # Optionally mark each of the building sites approved by
    # the city council
    if show_grid:
        for site_name, location in sites:
            goto(location)
            dot(5)
            goto(location[0] - (site_width // 2), location[1])
            setheading(0)
            pendown()
            forward(site_width)
            penup()
            goto(location[0] - 40, location[1] - 17)
            write(site_name + ': ' + str(location), font = grid_font)
     
    # Reset everything ready for the student's solution
    pencolor('black')
    width(1)
    penup()
    home()
    tracer(True)


# End the program and release the drawing canvas.
# By default the cursor (turtle) is hidden when the program
# ends - call the function with False as the argument to
# prevent this.
def release_drawing_canvas(hide_cursor = True):
    tracer(True) # ensure any drawing in progress is displayed
    if hide_cursor:
        hideturtle()
    done()
    
#
#--------------------------------------------------------------------#



#-----Test Data for Use During Code Development----------------------#
#
# The "fixed" data sets in this section are provided to help you
# develop and test your code.  You can use them as the argument to
# the build_city function while perfecting your solution.  However,
# they will NOT be used to assess your program.  Your solution will
# be assessed using the random_plan function appearing below.  Your
# program must work correctly for any data set generated by the
# random_plan function.
#
# Each of the data sets below is a list specifying a set of
# buildings to be erected.  Each specification consists of the
# following parts:
#
# a) The site on which to erect the building, from Site 1 to 10.
# b) The style of building to be erected, from style 'A' to 'D'.
# c) The number of floors to be constructed, from 1 to 10.
# d) An extra value, either 'X' or 'O', whose purpose will be
#    revealed only in Part B of the assignment.  You should
#    ignore it while completing Part A.
#

# Each of these data sets draws just one building in each of the
# four styles
fixed_plan_1 = [[1, 'A', 6, 'O']]
fixed_plan_2 = [[2, 'B', 7, 'O']]
fixed_plan_3 = [[3, 'C', 5, 'O']]
fixed_plan_4 = [[4, 'D', 4, 'O']]
fixed_plan_5 = [[1, 'A', 9, 'X']]
fixed_plan_6 = [[2, 'B', 2, 'X']]
fixed_plan_7 = [[3, 'C', 3, 'X']]
fixed_plan_8 = [[4, 'D', 6, 'X']]

# Each of the following data sets draws just one style of
# building but at three different sizes, including the maximum
# (so that you can check your building's maximum height against
# the height limit imposed by the city council)
fixed_plan_9 = [[1, 'A', 10, 'O'], [2, 'A', 5, 'O'], [3, 'A', 1, 'O']]
fixed_plan_10 = [[1, 'B', 10, 'O'], [2, 'B', 5, 'O'], [3, 'B', 1, 'O']]
fixed_plan_11 = [[1, 'C', 10, 'O'], [2, 'C', 5, 'O'], [3, 'C', 1, 'O']]
fixed_plan_12 = [[1, 'D', 10, 'O'], [2, 'D', 5, 'O'], [3, 'D', 1, 'O']]
fixed_plan_13 = [[1, 'A', 10, 'X'], [2, 'A', 5, 'X'], [3, 'A', 1, 'X']]
fixed_plan_14 = [[1, 'B', 10, 'X'], [2, 'B', 5, 'X'], [3, 'B', 1, 'X']]
fixed_plan_15 = [[1, 'C', 10, 'X'], [2, 'C', 5, 'X'], [3, 'C', 1, 'X']]
fixed_plan_16 = [[1, 'D', 10, 'X'], [2, 'D', 5, 'X'], [3, 'D', 1, 'X']]

# Each of the following data sets draws a complete cityscape
# involving each style of building at least once. There is
# no pattern to them, they are simply specific examples of the
# kind of data returned by the random_plan function which will be
# used to assess your solution. Your program must work for any value
# that can be returned by the random_plan function, not just these
# fixed data sets.
fixed_plan_17 = \
         [[1, 'D', 2, 'O'],
          [2, 'B', 7, 'O'],
          [5, 'C', 6, 'O'],
          [6, 'A', 4, 'O']]
fixed_plan_18 = \
         [[1, 'D', 6, 'O'],
          [3, 'C', 5, 'O'],
          [4, 'B', 3, 'O'],
          [9, 'A', 9, 'O'],
          [10, 'D', 2, 'O']]
fixed_plan_19 = \
         [[5, 'C', 6, 'O'],
          [6, 'B', 9, 'O'],
          [7, 'A', 5, 'O'],
          [8, 'A', 7, 'O'],
          [9, 'D', 4, 'O']]
fixed_plan_20 = \
         [[1, 'A', 4, 'O'],
          [2, 'B', 4, 'O'],
          [3, 'A', 5, 'O'],
          [4, 'D', 7, 'O'],
          [10, 'B', 10, 'O']]
fixed_plan_21 = \
         [[1, 'B', 6, 'O'],
          [3, 'A', 4, 'O'],
          [4, 'C', 4, 'O'],
          [6, 'A', 8, 'O'],
          [8, 'C', 7, 'O'],
          [9, 'B', 5, 'O'],
          [10, 'D', 3, 'O']]
fixed_plan_22 = \
         [[1, 'A', 10, 'O'],
          [2, 'A', 9, 'O'],
          [3, 'C', 10, 'O'],
          [4, 'B', 5, 'O'],
          [5, 'B', 7, 'O'],
          [6, 'B', 9, 'O'],
          [7, 'C', 2, 'O'],
          [8, 'C', 4, 'O'],
          [9, 'A', 6, 'O'],
          [10, 'D', 7, 'O']]
fixed_plan_23 = \
         [[3, 'A', 8, 'O'],
          [4, 'C', 8, 'O'],
          [5, 'B', 4, 'O'],
          [6, 'D', 5, 'O'],
          [7, 'C', 5, 'X'],
          [8, 'A', 3, 'X'],
          [9, 'D', 2, 'X']]
fixed_plan_24 = \
         [[2, 'C', 3, 'O'],
          [3, 'B', 1, 'O'],
          [4, 'C', 3, 'X'],
          [5, 'C', 1, 'O'],
          [6, 'D', 2, 'O'],
          [7, 'B', 1, 'O'],
          [8, 'D', 2, 'O'],
          [9, 'C', 7, 'O'],
          [10, 'A', 1, 'X']]
fixed_plan_25 = \
         [[1, 'B', 7, 'X'],
          [3, 'C', 1, 'O'],
          [6, 'D', 3, 'O'],
          [7, 'A', 7, 'O'],
          [8, 'D', 3, 'X'],
          [9, 'C', 7, 'O'],
          [10, 'C', 9, 'X']]
fixed_plan_26 = \
         [[1, 'A', 6, 'O'],
          [2, 'A', 2, 'O'],
          [3, 'A', 9, 'X'],
          [4, 'D', 1, 'X'],
          [5, 'C', 7, 'O'],
          [6, 'D', 6, 'O'],
          [7, 'B', 5, 'O'],
          [8, 'A', 1, 'O'],
          [9, 'D', 10, 'X'],
          [10, 'A', 6, 'O']]
 
#
#--------------------------------------------------------------------#



#-----Function for Assessing Your Solution---------------------------#
#
# The function in this section will be used to mark your solution.
# Do not change any of the code in this section.
#
# The following function creates a random data set specifying a city
# to be built.  Your program must work for any data set returned by
# this function.  The results returned by calling this function will
# be used as the argument to your build_city function during marking.
# For convenience during code development and marking this function
# also prints the plan for the city to be built to the shell window.
#

def random_plan(print_plan = True):
    building_probability = 70 # percent
    option_probability = 20 # percent
    from random import randint, choice
    # Create a random list of building instructions
    city_plan = []
    for site in range(1, len(sites) + 1): # consider each building site
        if randint(1, 100) <= building_probability: # decide whether to build here
            style = choice(['A', 'B', 'C', 'D']) # choose building style
            num_floors = randint(1, 10) # choose number of floors
            if randint(1, 100) <= option_probability: # decide on option's value
                option = 'X'
            else:
                option = 'O'
            city_plan.append([site, style, num_floors, option])
    # Optionally print the result to the shell window
    if print_plan:
        print('\nBuildings to be constructed\n' +
              '(site, style, no. floors, option):\n\n',
              str(city_plan).replace('],', '],\n '))
    # Return the result to the student's build_city function
    return city_plan

#
#--------------------------------------------------------------------#



#-----Student's Solution---------------------------------------------#
#
#  Complete the assignment by replacing the dummy function below with
#  your own "build_city" function.
#

def con_sign(): #daws a sign showing the building is under construction for Part B
    setheading(0)
    penup()
    forward(30)
    pendown()
    begin_fill()
    fillcolor("orangered")
    pencolor("black")
    width(4)
    forward(80)
    left(120)
    forward(80)
    left(120)
    forward(80)
    end_fill()
    penup()
    left(120)
    forward(60)
    left(90)
    forward(23)
    pendown()
    pencolor("black")
    begin_fill()
    fillcolor("Crimson")
    circle(20)
    end_fill()
    penup()
    backward(8)
    left(70)
    pendown()
    forward(40)
    penup()
    #reset
    pencolor("black")
    width(1)


def ground_style_1(x,y): #draws ground floor for design A
    penup()
    goto(x,y)
    setheading(0)
    backward(125)
    pendown()
    pencolor("purple")
    begin_fill()
    fillcolor("Crimson")
    forward(250)
    left(90)
    forward(50)
    left(90)
    forward(250)
    left(90)
    forward(50)
    left(90)
    end_fill()
    #door
    begin_fill()
    fillcolor("gray")
    penup()
    forward(65)
    left(90)
    pencolor("black")
    pendown()
    forward(50)
    right(90)
    forward(125)
    right(90)
    forward(50)
    end_fill()
    #door line
    penup()
    backward(65)
    right(90)
    forward(65)
    left(90)
    pendown()
    forward(65)
    #back to top corner
    penup()
    left(90)
    backward(125)
    left(90)
    forward(50)
    right(90)
    #reset
    pencolor("black")
    width(1)


def floor_style_1(): #Draws floors for design A
    pendown()
    setheading(0)
    pencolor("purple")
    begin_fill()
    fillcolor("Crimson")
    forward(250)
    left(90)
    forward(50)
    left(90)
    forward(250)
    left(90)
    forward(50)
    end_fill()
    #window
    penup()
    backward(25)
    left(90)
    forward(10)
    left(90)
    pendown()
    begin_fill()
    fillcolor("GhostWhite")
    forward(20)
    right(90)
    forward(225)
    right(90)
    forward(40)
    right(90)
    forward(225)
    right(90)
    forward(20)
    end_fill()
    #back to corner
    penup()
    backward(25)
    left(90)
    forward(10)
    right(90)
    forward(50)
    pencolor("black")
    width(1)

def roof_style_1(con): #draws roof for design A
    if con == 'O':
        width(3)
        setheading(0)
        penup()
        forward(80)
        left(90)
        pendown()
        forward(25)
        begin_fill()
        fillcolor("Grey")
        left(90)
        forward(80)
        right(90)
        forward(100)
        right(90)
        forward(250)
        right(90)
        forward(100)
        right(90)
        forward(200)
        end_fill()
        penup()
        backward(125)
        left(90)
        pendown()
        forward(25)
        penup()
        #color("Crimson")
        penup()
        right(180)
        forward(80)
        left(90)
        forward(65)
        write("WOW", font=("size=100"))
    elif con == 'X':
        con_sign()
    #reset
    pen("black")
    width(1)
    penup()

def ground_style_2(x,y): #draws ground for Design B
    setheading(0)
    goto(x,y)
    penup()
    backward(75)
    pendown()
    pencolor("black")
    begin_fill()
    fillcolor("medium blue")
    forward(150)
    left(90)
    forward(50)
    left(90)
    forward(150)
    left(90)
    forward(50)
    end_fill()
    #draw door
    left(90)
    penup()
    forward(25)
    left(90)
    pendown()
    width(4)
    begin_fill()
    fillcolor("silver")
    circle(-50, extent=180)
    right(90)
    forward(100)
    left(180)
    end_fill()
    #draw door lines
    penup()
    forward(10)
    left(90)
    width(4)
    pendown()
    forward(25)
    backward(25)
    right(90)
    penup()
    forward(25)
    left(90)
    pendown()
    forward(45)
    penup()
    backward(45)
    right(90)
    forward(25)
    left(90)
    pendown()
    forward(48)
    penup()
    backward(48)
    right(90)
    forward(25)
    left(90)
    pendown()
    forward(30)
    #send curser back to corner
    penup()
    backward(30)
    left(90)
    forward(110)
    right(90)
    forward(50)
    #reset
    pencolor("black")
    width(1)
    
def floor_style_2(): #draws floor for design B
    pendown()
    setheading(0)
    begin_fill()
    fillcolor("medium blue")
    forward(150)
    left(90)
    forward(50)
    left(90)
    forward(150)
    left(90)
    forward(50)
    end_fill()
    #window
    penup()
    left(90)
    fillcolor("mintcream")
    forward(40)
    left(90)
    forward(5)
    begin_fill()
    pencolor("sienna")
    width(3)
    pendown()
    forward(35)
    right(90)
    forward(60)
    right(90)
    forward(35)
    right(90)
    forward(60)
    end_fill()
    penup()
    right(180)
    forward(30)
    left(90)
    pendown()
    pencolor("sienna")
    width(3)
    forward(35)
    penup()
    backward(15)
    right(90)
    backward(30)
    pendown()
    forward(60)
    #back to corner
    penup()
    left(90)
    backward(25)
    left(90)
    forward(100)
    right(90)
    forward(50)
    #reset
    pencolor("black")
    width(1)

def roof_style_2(con): #draws roof for design B
    if con == 'O':
        pendown()
        setheading(0)
        forward(150)
        backward(150)
        left(90)
        pencolor("black")
        begin_fill()
        fillcolor("medium blue")
        forward(25)
        right(90)
        forward(30)
        left(90)
        forward(25)
        right(90)
        forward(30)
        left(90)
        forward(20)
        right(90)
        forward(25)
        right(90)
        forward(20)
        left(90)
        forward(30)
        right(90)
        forward(25)
        left(90)
        forward(35)
        right(90)
        forward(25)
        end_fill()
    elif con == 'X':
        con_sign()
    #reset
    pen("black")
    width(1)
    penup()

def ground_style_3(x,y): #draws ground for design C
    setheading(0)
    penup()
    goto(x,y)
    backward(100)
    pendown()
    setheading(0)
    begin_fill()
    fillcolor("dim gray")
    forward(200)
    left(90)
    forward(50)
    left(90)
    forward(200)
    left(90)
    forward(50)
    end_fill()
    #move pen
    penup()
    left(90)
    forward(50)
    left(90)
    pendown()
    #stairs
    forward(40)
    right(90)
    forward(100)
    right(90)
    forward(40)
    backward(25)
    right(90)
    forward(100)
    left(90)
    forward(15)
    left(90)
    forward(100)
    #move pen
    penup()
    right(90)
    forward(10)
    right(90)
    forward(150)
    right(90)
    forward(50)
    #reset
    pencolor("black")
    width(1)


def floor_style_3(): #draws floors for design C
    pendown()
    setheading(0)
    begin_fill()
    fillcolor("dim gray")
    forward(200)
    left(90)
    forward(50)
    left(90)
    forward(200)
    left(90)
    forward(50)
    end_fill()
    #move pen
    penup()
    left(90)
    forward(15)
    left(90)
    forward(5)
    right(90)
    #windows
    for window in range(5): #loop draws the window 5 times instead of writing code over and over
        setheading(0)
        pendown()
        pencolor("black")
        width(1.5)
        begin_fill()
        fillcolor("steel blue")
        forward(25)
        left(90)
        forward(40)
        left(90)
        forward(25)
        left(90)
        forward(40)
        end_fill()
        penup()
        left(90)
        forward(35)
        pendown()
    #move pen
    penup()
    backward(190)
    left(90)
    forward(45)
    #reset
    pencolor("black")
    width(1)

def roof_style_3(con): #draws roof for design C
    if con == 'O':
        pendown()
        setheading(0)
        begin_fill()
        fillcolor("dim gray")
        forward(200)
        left(120)
        forward(200)
        left(120)
        forward(200)
        end_fill()
        #move pen
        penup()
        left(120)
        forward(100)
        left(90)
        forward(20)
        right(90)
        #window
        begin_fill()
        fillcolor("steel blue")
        pendown()
        circle(45)
        left(90)
        end_fill()
        width(1.5)
        forward(90)
        backward(45)
        left(90)
        backward(45)
        forward(90)
        penup()
    elif con == 'X':
        con_sign()
    #reset
    pen("black")
    width(1)
    penup()

def ground_style_4(x,y): #draws ground floor for design D
    penup()
    goto(x,y)
    setheading(0)
    backward(100)
    pendown()
    begin_fill()
    fillcolor("brown")
    forward(200)
    left(90)
    forward(50)
    left(90)
    forward(200)
    left(90)
    forward(50)
    end_fill()
    #move pen
    left(90)
    forward(50)
    left(90)
    #door
    begin_fill()
    fillcolor("dim gray")
    forward(45)
    right(90)
    forward(100)
    right(90)
    forward(45)
    end_fill()
    backward(45)
    right(90)
    forward(50)
    left(90)
    forward(45)
    #door knobs
    penup()
    backward(22)
    right(90)
    forward(5)
    pendown()
    dot(5)
    penup()
    right(180)
    forward(10)
    pendown()
    dot(5)
    #move pen
    penup()
    backward(105)
    left(90)
    forward(28)
    #reset
    pencolor("black")
    width(1)

def floor_style_4(): #draws middle floors for design D
    pendown()
    setheading(0)
    begin_fill()
    fillcolor("brown")
    forward(200)
    left(90)
    forward(50)
    left(90)
    forward(200)
    left(90)
    forward(50)
    end_fill()
    #move pen
    penup()
    left(90)
    left(90)
    forward(5)
    right(90)
    forward(5)
    pendown()
    #windows
    for window in range(5):
        setheading(0)
        pendown()
        pencolor("black")
        width(1.5)
        begin_fill()
        fillcolor("dim gray")
        forward(25)
        left(90)
        forward(40)
        left(90)
        forward(25)
        left(90)
        forward(40)
        end_fill()
        penup()
        left(90)
        forward(41)
        pendown()
    #move pen
    penup()
    backward(210)
    left(90)
    forward(45)
    #reset
    pencolor("black")
    width(1)

def roof_style_4(con): #draws roof for design D
    if con == 'O':
        pendown()
        setheading(0)
        begin_fill()
        fillcolor("brown")
        left(90)
        circle(-100, extent=180)
        left(90)
        end_fill()
    elif con == 'X':
        con_sign()
    #reset
    pen("black")
    width(1)
    penup()
        


    
def draw_buildingA(x,y, height, con): #builds design A
    ground_style_1(x,y)
    for build_A in range (height):
        height = height - 2 #Attempt to have buildings below max height. Subtracting 2 because there are two floors that are not considered by random_plan
        floor_style_1()
    roof_style_1(con)
   

def draw_buildingB(x,y, height, con): #builds design B
    ground_style_2(x,y)
    for build_B in range (height):
        heght = height - 2
        floor_style_2()
    roof_style_2(con)

def draw_buildingC(x,y, height, con): #builds design C
    ground_style_3(x,y)  
    for build_C in range(height):
        height = height - 2
        floor_style_3()
    roof_style_3(con)

def draw_buildingD(x,y, height, con): #builds design D
    ground_style_4(x,y)
    for build_D in range(5):
        height = height -2
        floor_style_4()
    roof_style_4(con)
    
# Erect buildings as per the provided city plan
def build_city(dummy_parameter):
    for site in dummy_parameter:
        loc =  site[0]
        style =site[1]
        height = site[2]
        con = site[3]

        if loc  == 1:
            x  = -225
            y = 0
        elif loc == 2:
            x = 25
            y = 0
        elif loc == 3:
            x = 275
            y = 0
        elif loc == 4:
            x = -375
            y = -25
        elif loc == 5:
            x = -125
            y = -25
        elif loc == 6:
            x = 125
            y = -25
        elif loc == 7:
            x = 375
            y = -25
        elif loc == 8:
            x = -275
            y = -50
        elif loc == 9:
            x = -25
            y = -50
        elif loc == 10:
            x = 225
            y = -50
        
        #Calls the appropriate building 
        if style == 'A': 
            draw_buildingA(x,y, height, con)
        elif style == 'B':
            draw_buildingB(x,y, height, con)
        elif style == 'C':
            draw_buildingC(x,y, height, con)
        elif style == 'D':
            draw_buildingD(x,y, height, con)
            

      



#
#--------------------------------------------------------------------#



#-----Main Program---------------------------------------------------#
#
# This main program sets up the background, ready for you to start
# building your city.  Do not change any of this code except
# as indicated by the comments marked '*****'.
#

# Set up the drawing canvas
# ***** Change the default argument to False if you don't want to
# ***** display the coordinates and building sites
create_drawing_canvas()

# Control the drawing speed
# ***** Modify the following argument if you want to adjust
# ***** the drawing speed
speed('slow')

# Decide whether or not to show the drawing being done step-by-step
# ***** Set the following argument to False if you don't want to wait
# ***** while the cursor moves around the screen
tracer(False)

# Give the drawing canvas a title
# ***** Replace this title with your name and/or a description of
# ***** your city
title("Various buildings")

### Call the student's function to build the city
### ***** While developing your program you can call the build_city
### ***** function with one of the "fixed" data sets, but your
### ***** final solution must work with "random_plan()" as the
### ***** argument to the build_city function.  Your program must
### ***** work for any data set that can be returned by the
### ***** random_plan function.
# build_city(fixed_plan_1) # <-- used for code development only, not marking
build_city(random_plan()) # <-- used for assessment

    
# Exit gracefully
# ***** Change the default argument to False if you want the
# ***** cursor (turtle) to remain visible at the end of the
# ***** program as a debugging aid
release_drawing_canvas()

#
#--------------------------------------------------------------------#


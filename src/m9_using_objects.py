"""
This module lets you practice  ** using objects **, including:
  -- CONSTRUCTING objects,
  -- applying METHODS to them, and
  -- accessing their DATA via INSTANCE VARIABLES

Authors: David Mutchler, Vibha Alangar, Matt Boutell, Dave Fisher, Mark Hays,
         Aaron Wilkin, their colleagues, and Daniel Su.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.

import rosegraphics as rg
import math


def main():
    """ Calls the other functions to demonstrate and/or test them. """
    # Test your functions by putting calls to them here:
    two_circles()
    circle_and_rectangle()
    lines()


def two_circles():
    """
    -- Constructs an rg.RoseWindow.
    -- Constructs and draws two rg.Circle objects on the window
         such that:
           -- They fit in the window and are easily visible.
           -- They have different radii.
           -- One is filled with some color and one is not filled.
    -- Waits for the user to press the mouse, then closes the window.
    """
    # -------------------------------------------------------------------------
    # DONE: 2. Implement this function, per its green doc-string above.
    #    -- ANY two rg.Circle objects that meet the criteria are fine.
    #    -- File  COLORS.pdf  lists all legal color-names.
    # Put a statement in   main   to test this function
    #    (by calling this function).
    # -------------------------------------------------------------------------
    window = rg.RoseWindow()
    circle1 = rg.Circle(rg.Point(100,100),50)
    circle1.fill_color = 'red'
    circle2 = rg.Circle(rg.Point(200,200),60)
    circle1.attach_to(window)
    circle2.attach_to(window)
    window.render()
    window.close_on_mouse_click()



def circle_and_rectangle():
    """
    -- Constructs an rg.RoseWindow.
    -- Constructs and draws a rg.Circle and rg.Rectangle
       on the window such that:
          -- They fit in the window and are easily visible.
          -- The rg.Circle is filled with 'blue'
    -- Prints (on the console, on SEPARATE lines) the following data
         associated with your rg.Circle:
          -- Its outline thickness.
          -- Its fill color.
          -- Its center.
          -- Its center's x coordinate.
          -- Its center's y coordinate.
    -- Prints (on the console, on SEPARATE lines) the same data
         but for your rg.Rectangle.
    -- Waits for the user to press the mouse, then closes the window.

    Here is an example of the output on the console,
    for one particular circle and rectangle:
           1
           blue
           Point(180.0, 115.0)
           180
           115
           1
           None
           Point(75.0, 150.0)
           75.0
           150.0
    """
    # -------------------------------------------------------------------------
    # DONE: 3. Implement this function, per its green doc-string above.
    #   -- ANY objects that meet the criteria are fine.
    # Put a statement in   main   to test this function
    #    (by calling this function).
    #
    # IMPORTANT: Use the DOT TRICK to guess the names of the relevant
    #       instance variables for outline thickness, etc.
    # -------------------------------------------------------------------------
    window = rg.RoseWindow()
    cthick = 2
    cx = 100
    cy = 100
    ccolor = 'blue'
    ccenter = rg.Point(cx, cy)
    rthick = 4
    rx1 = 150
    ry1 = 150
    rx2 = 300
    ry2 = 250
    rcenterx = math.fabs(rx1 + rx2)/2
    rcentery = math.fabs(ry1 + ry2)/2
    rcenter = rg.Point(rcenterx, rcentery)
    rcolor = 'red'

    print("--------------------------------------------------------------------------")
    print("Circle Variables")
    print("--------------------------------------------------------------------------")
    print("Outline Thickness:", cthick)
    print("Fill Color:", ccolor)
    print("Center:", ccenter)
    print("Center's x Coordinate:", cx)
    print("Center's y Coordinate:", cy)
    print("--------------------------------------------------------------------------")
    print("Rectangle Variables")
    print("--------------------------------------------------------------------------")
    print("Outline Thickness:", rthick)
    print("Fill Color:", rcolor)
    print("Center:", rcenter)
    print("Center's x Coordinate:", rcenterx)
    print("Center's y Coordinate:", rcentery)

    circle = rg.Circle(ccenter,50)
    circle.fill_color = ccolor
    circle.outline_thickness = cthick
    rectangle = rg.Rectangle(rg.Point(rx1,ry1),rg.Point(rx2,ry2))
    rectangle.outline_thickness = rthick
    rectangle.fill_color = rcolor

    circle.attach_to(window)
    rectangle.attach_to(window)
    window.render()
    window.close_on_mouse_click()



def lines():
    """
    -- Constructs a rg.RoseWindow.
    -- Constructs and draws on the window two rg.Lines such that:
          -- They both fit in the window and are easily visible.
          -- One rg.Line has the default thickness.
          -- The other rg.Line is thicker (i.e., has a bigger width).
    -- Uses a rg.Line method to get the midpoint (center) of the
         thicker rg.Line.
    -- Then prints (on the console, on SEPARATE lines):
         -- the midpoint itself
         -- the x-coordinate of the midpoint
         -- the y-coordinate of the midpoint

       Here is an example of the output on the console, if the two
       endpoints of the thicker line are at (100, 100) and (121, 200):
            Point(110.5, 150.0)
            110.5
            150.0

    -- Waits for the user to press the mouse, then closes the window.
    """
    # DONE: 4. Implement and test this function.
    window = rg.RoseWindow()
    lineAx1 = 100
    lineAy1 = 100
    lineAx2 = 10
    lineAy2 = 10
    lineAmid = rg.Point(math.fabs((lineAx1 + lineAx2))/2, math.fabs((lineAy1 + lineAy2)/2))
    lineAmidx = math.fabs((lineAx1 + lineAx2))/2
    lineAmidy = math.fabs((lineAy1 + lineAy2))/2
    lineBx1 = 120
    lineBy1 = 200
    lineBx2 = 350
    lineBy2 = 220
    lineBmid = rg.Point(math.fabs((lineBx1 + lineBx2)) / 2, math.fabs((lineBy1 + lineBy2) / 2))
    lineBmidx = math.fabs((lineBx1 + lineBx2)) / 2
    lineBmidy = math.fabs((lineBy1 + lineBy2)) / 2

    print("--------------------------------------------------------------------------")
    print("Line A Variables")
    print("--------------------------------------------------------------------------")
    print("Midpoint:", lineAmid)
    print("X-Coordinate of Midpoint:", lineAmidx)
    print("Y-Coordinate of Midpoint:", lineAmidy)
    print("--------------------------------------------------------------------------")
    print("Line B Variables")
    print("--------------------------------------------------------------------------")
    print("Midpoint:", lineBmid)
    print("X-Coordinate of Midpoint:", lineBmidx)
    print("Y-Coordinate of Midpoint:", lineBmidy)

    lineA = rg.Line(rg.Point(lineAx1,lineAy1),rg.Point(lineAx2,lineAy2))
    lineB = rg.Line(rg.Point(lineBx1,lineBy1),rg.Point(lineBx2,lineBy2))
    lineB.thickness = 4
    lineA.attach_to(window)
    lineB.attach_to(window)
    window.render()
    window.close_on_mouse_click()



# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()

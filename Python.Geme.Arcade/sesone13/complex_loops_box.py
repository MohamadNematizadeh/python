
"""
Example "Arcade" library code.

Showing how to do nested loops.

If Python and Arcade are installed, this example can be run from the command line with:
python -m arcade.examples.complex_loops_box
"""

# Library imports
import arcade

COLUMN_SPACING = 20
ROW_SPACING = 20
LEFT_MARGIN = 110
BOTTOM_MARGIN = 110
SCREEN_LOKE = "img/128.png"
DAMATION = 10


# Open the window and set the background
arcade.open_window(400, 400, "Complex Loops Box")



arcade.set_background_color(arcade.color.WHITE)

# Start the render process. This must be done before any drawing commands.
arcade.start_render()

# Loop for each row
for row in range(10):
      for column in range(10):
         # Calculate our location
         x = column * COLUMN_SPACING + LEFT_MARGIN
         y = row * ROW_SPACING + BOTTOM_MARGIN

         # Draw the item
         if (row + column)%2 == 0:
             color_draw = arcade.color.RED
         else:
            color_draw = arcade.color.BLUE
         arcade.draw_rectangle_filled(x, y, 10, 10, color_draw, 45)
# Finish the render.
arcade.finish_render()

# Keep the window up until someone closes it.
arcade.run()
import sys
sys.path.append("/home/srush/Projects/diagrams/venv/lib/python3.9/site-packages")
import math
from chalk import *

# ## Diagram Creation

# ### circle

help(circle)

#

circle(1) + circle(0.5)

# ### arc

help(arc)

#

quarter = math.pi / 2
arc(1, 0, quarter) 

#

arc(1, 0, quarter) + arc(1, 2 * quarter, 3 * quarter) 


# ### arc_between

help(arc_between)

#

arc_between((0, 0), (1, 0), 1)

# ### polygon

help(polygon)

#

polygon(8, 2)


# ### square

help(square)

#

square(1)


# ### triangle

help(triangle)

#

triangle(1)


# ### rectangle

help(rectangle)

#

rectangle(8, 2, 0.5)



# ### make_path

help(make_path)

#

make_path([(0, 0), (0, 1), (1, 1), (1, 2)])

# ### text

help(text)

#

text("hello", 0.2)


# ## Alignment


# ### Diagram.show_origin

help(Diagram.show_origin)

#

triangle(1).show_origin()

# ### Diagram.show_bounding_box

help(Diagram.show_bounding_box)

#

triangle(1).show_bounding_box()

# ### Diagram.align_t

help(Diagram.align_t)

#

triangle(1).align_t().show_bounding_box().show_origin()

# ### Diagram.align_r

help(Diagram.align_r)

#

triangle(1).align_r().show_bounding_box().show_origin()

# ### Diagram.center_xy

help(Diagram.center_xy)

#

triangle(1).center_xy().show_bounding_box().show_origin()


# ### Diagram.pad

help(Diagram.pad)

#

triangle(1).pad(0.5).show_bounding_box().show_origin()




# ## Combinators

# ### above

help(above)

#

diagram = triangle(1) / square(1)
diagram

#

diagram.show_bounding_box().show_origin()


# ### atop

help(atop)

# Example 1 - Atop at origin

diagram = square(1) + triangle(1)
diagram

#

diagram.show_bounding_box().show_origin()

# Example 2 - Align then atop origin

s = square(1).align_r().align_b().show_origin()
t = triangle(1).align_l().align_t().show_origin()
s

#

t

#

s + t

# ### beside

help(beside)

#

diagram = triangle(1) | square(1)
diagram

#

triangle(1).show_origin() | square(1).show_origin()

#

diagram.show_origin()


# ### vcat

help(vcat)

#

vcat([triangle(1), square(1), triangle(1)], 0.2)

# ### concat

help(concat)

#

concat([triangle(1), square(1), triangle(1)])


# ### hcat

help(hcat)

#

hcat([triangle(1), square(1), triangle(1)], 0.2)

# ## Transformations


# ## Style



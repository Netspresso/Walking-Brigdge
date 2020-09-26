import math


class Curve():

    # Velocity of growing curves
    v = 2.0 / math.pi

    # other lenght in meters:
    br_width = 0.5
    spacing = 0.2
    plinth = 0.15
    beam_width = 2.0 * plinth + 3.0 * spacing
    ibeam_height = -0.4
    obeam_height = -0.5
    plate_height = 0
    plate_bottom = 0.0
    pipe_diameter = 0.4
    range_a = 4.5 * math.pi
    range_b = range_a
    step = 0.1

    slow_step = math.pi / 4.0
    beam_distance = 1.5
    pr_height = -0.15
    # thats all

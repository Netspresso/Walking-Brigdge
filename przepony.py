import apex
from apex.construct import Point3D, Point2D
from apex.geometry import createPointXYZ, createCurve3DNurb
import math


apex.setScriptUnitSystem(unitSystemName = r'''mm-kg-s-N''')
applicationSettingsGeometry = apex.setting.ApplicationSettingsGeometry()
applicationSettingsGeometry.createGeometryInNewPart = apex.setting.CreateGeometryInNewPart.CurrentPart
applicationSettingsGeometry.geometryTessellationIsWatertight = False
applicationSettingsGeometry.geometryEdgeTesselationTolerance = apex.setting.GeometryTessellationTolerance.Medium
applicationSettingsGeometry.geometryFaceTesselationTolerance = apex.setting.GeometryTessellationTolerance.Medium
apex.setting.setApplicationSettingsGeometry(applicationSettingsGeometry = applicationSettingsGeometry)
model_1 = apex.currentModel()

import math


class Curves:
    # Class defining curves A

    def __init__(self, a, b, Velocity, Distance, ListPoint):
        t = 0
        count = len(a)
        z = range(0, count)
        for i in z:
            Curves.x = a[i] * math.cos(t) - (5 * t) / (4 * math.pi) + 15
            Curves.y = b[i] * math.sin(t)
            Curves.z = Velocity * t + Distance
            ListPoint.Add(Point.Create(Curves.x, Curves.y, Curves.z))
            t += math.pi / 4.0


class Curves_B:

    # Class defining curves B

    def __init__(self, component, Distance, ListPoint):
        x = 9.375
        while x >= -8.0:
            Curves_B.x = x
            Curves_B.y = 1.875 + component
            Curves_B.z = 9 + Distance
            ListPoint.Add(Point.Create(Curves_B.x, Curves_B.y, Curves_B.z))
            x -= 0.01


class Curves_D:

    def __init__(self, component, Distance, ListPoint):
        x = -9.375
        while x <= 8.0:
            Curves.x = x
            Curves.y = -1.875 - component
            Curves.z = 9 + Distance
            ListPoint.Add(Point.Create(Curves.x, Curves.y, Curves.z))
            x += 0.01


class Curves_C:

    def __init__(self, a, b, Velocity, Distance, ListPoint):
        t = 0
        count = len(a)
        z = range(0, count)
        for i in z:
            Curves.x = -a[i] * math.cos(t) + (5 * t) / (4 * math.pi) - 15
            Curves.y = -b[i] * math.sin(t)
            Curves.z = Velocity * t + Distance
            ListPoint.Add(Point.Create(Curves.x, Curves.y, Curves.z))
            t += math.pi / 4.0


def a(tmax, Step, component):
    """Inner radius(f) (from center to the beam)"""
    radius = []

    t = 0
    while t <= tmax:
        radius.append((-5 / (4 * math.pi)) * t + 10 + component)
        t += Step
    return radius


def b(tmax, Step, component):
    """distance between borders of beams """
    radius = []

    t = 0
    while t <= tmax:
        radius.append((-5 / (4 * math.pi)) * t + 7.5 + component)
        t += Step

    return radius


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
range_b = 4.5 * math.pi
step = 0.01
slow_step = math.pi / 4.0
beam_distance = 1.5
pr_height = -0.15
# thats all

# Lists of point for all curves
ptList_p = []

n_of_curve = 20
ncurve = []
curveSegment = []
designCurve = []

for i in range(0, n_of_curve):
    ptList_p.append(List[Point]())

Curves(a(range_a, slow_step, -br_width), b(range_b, slow_step, -br_width), v, 0, ptList_p[0])
Curves(a(range_a, slow_step, -br_width), b(range_b, slow_step, -br_width), v, pr_height, ptList_p[1])
Curves(a(range_a, slow_step, plinth), b(range_b, slow_step, plinth), v, ibeam_height, ptList_p[2])
Curves(a(range_a, slow_step, spacing + plinth), b(range_b, slow_step, spacing + plinth), v, ibeam_height, ptList_p[3])
Curves(a(range_a, slow_step, 2.0 * spacing + plinth), b(range_b, slow_step, 2.0 * spacing + plinth), v, ibeam_height,
       ptList_p[4])
Curves(a(range_a, slow_step, 3.0 * spacing + plinth), b(range_b, slow_step, 3.0 * spacing + plinth), v, ibeam_height,
       ptList_p[5])
Curves(a(range_a, slow_step, beam_distance + plinth), b(range_b, slow_step, beam_distance + plinth), v, obeam_height,
       ptList_p[6])
Curves(a(range_a, slow_step, beam_distance + plinth + spacing), b(range_b, slow_step, beam_distance + plinth + spacing),
       v, obeam_height, ptList_p[7])
Curves(a(range_a, slow_step, beam_distance + plinth + 2.0 * spacing),
       b(range_b, slow_step, beam_distance + plinth + 2.0 * spacing), v, obeam_height, ptList_p[8])
Curves(a(range_a, slow_step, beam_distance + plinth + 3.0 * spacing),
       b(range_b, slow_step, beam_distance + plinth + 3.0 * spacing), v, obeam_height, ptList_p[9])
Curves(a(range_a, slow_step, beam_distance + 2.0 * plinth + 3.0 * spacing + br_width),
       b(range_b, slow_step, beam_distance + 2.0 * plinth + 3.0 * spacing + br_width), v, pr_height, ptList_p[10])
Curves(a(range_a, slow_step, beam_distance + 2.0 * plinth + 3.0 * spacing + br_width),
       b(range_b, slow_step, beam_distance + 2.0 * plinth + 3.0 * spacing + br_width), v, 0, ptList_p[11])
Curves(a(range_a, slow_step, beam_distance + 2.0 * plinth + 3.0 * spacing),
       b(range_b, slow_step, beam_distance + 2.0 * plinth + 3.0 * spacing), v, 0, ptList_p[12])
Curves(a(range_a, slow_step, beam_distance + plinth + 2.0 * spacing),
       b(range_b, slow_step, beam_distance + plinth + 2.0 * spacing), v, 0, ptList_p[13])
Curves(a(range_a, slow_step, beam_distance + plinth + spacing), b(range_b, slow_step, beam_distance + plinth + spacing),
       v, 0, ptList_p[14])
Curves(a(range_a, slow_step, beam_distance), b(range_b, slow_step, beam_distance), v, 0, ptList_p[15])
Curves(a(range_a, slow_step, 3.0 * spacing + 2.0 * plinth), b(range_b, slow_step, 3.0 * spacing + 2.0 * plinth), v, 0,
       ptList_p[16])
Curves(a(range_a, slow_step, 2.0 * spacing + plinth), b(range_b, slow_step, 2.0 * spacing + plinth), v, 0, ptList_p[17])
Curves(a(range_a, slow_step, spacing + plinth), b(range_b, slow_step, spacing + plinth), v, 0, ptList_p[18])
Curves(a(range_a, slow_step, 0), b(range_b, slow_step, 0), v, 0, ptList_p[19])

'''
Curves_B(0, 0, ptList_p[0])
Curves_B(plinth, ibeam_height, ptList_p[1])
Curves_B(plinth + spacing, 0, ptList_p[2])
Curves_B(plinth + spacing, ibeam_height, ptList_p[3])
Curves_B(2.0 * spacing + plinth, 0, ptList_p[4])
Curves_B(2.0 * spacing + plinth, ibeam_height, ptList_p[5])
Curves_B(3.0 * spacing + 2.0 * plinth, 0, ptList_p[6])
Curves_B(3.0 * spacing + plinth, ibeam_height, ptList_p[7])
Curves_B(beam_distance, 0,   ptList_p[8])
Curves_B(beam_distance + plinth, obeam_height,   ptList_p[9])
Curves_B(beam_distance + plinth + spacing, 0,   ptList_p[10])
Curves_B(beam_distance + plinth + spacing, obeam_height,   ptList_p[11])
Curves_B(beam_distance + plinth + 2.0*spacing, 0,   ptList_p[12])
Curves_B(beam_distance + plinth + 2.0*spacing, obeam_height,   ptList_p[13])
Curves_B(beam_distance + 2.0*plinth + 3.0*spacing, 0,   ptList_p[14])
Curves_B( beam_distance + plinth + 3.0*spacing, obeam_height,   ptList_p[15])
Curves_B(beam_distance + beam_width + br_width, plate_height,   ptList_p[16])
Curves_B(-br_width, plate_height,   ptList_p[17])
'''

'''
Curves_C(a(range_a, slow_step, -br_width), b(range_b, slow_step, -br_width), v, 0, ptList_p[20])
Curves_C(a(range_a, slow_step, -br_width), b(range_b, slow_step, -br_width), v, pr_height, ptList_p[21])
Curves_C(a(range_a, slow_step, plinth), b(range_b, slow_step, plinth), v, ibeam_height, ptList_p[22])
Curves_C(a(range_a, slow_step, spacing + plinth), b(range_b, slow_step, spacing + plinth), v, ibeam_height, ptList_p[23])
Curves_C(a(range_a, slow_step, 2.0 * spacing + plinth), b(range_b, slow_step, 2.0 * spacing + plinth), v, ibeam_height, ptList_p[24])
Curves_C(a(range_a, slow_step, 3.0 * spacing + plinth), b(range_b, slow_step, 3.0 * spacing + plinth), v, ibeam_height, ptList_p[25])
Curves_C(a(range_a, slow_step, beam_distance + plinth),b(range_b, slow_step, beam_distance + plinth), v, obeam_height, ptList_p[26])
Curves_C(a(range_a, slow_step, beam_distance + plinth + spacing), b(range_b, slow_step, beam_distance + plinth + spacing), v, obeam_height,   ptList_p[27])
Curves_C(a(range_a, slow_step, beam_distance + plinth + 2.0 * spacing), b(range_b, slow_step, beam_distance + plinth + 2.0 * spacing), v, obeam_height,   ptList_p[28])
Curves_C(a(range_a, slow_step, beam_distance + plinth + 3.0 * spacing), b(range_b, slow_step, beam_distance + plinth + 3.0 * spacing), v, obeam_height,   ptList_p[29])
Curves_C(a(range_a, slow_step, beam_distance + 2.0 * plinth + 3.0 * spacing + br_width), b(range_b, slow_step, beam_distance + 2.0 * plinth + 3.0 * spacing + br_width), v, pr_height,   ptList_p[30])
Curves_C(a(range_a, slow_step, beam_distance + 2.0 * plinth + 3.0 * spacing + br_width), b(range_b, slow_step, beam_distance + 2.0 * plinth + 3.0 * spacing + br_width), v, 0,   ptList_p[31])
Curves_C(a(range_a, slow_step, beam_distance + 2.0*plinth + 3.0*spacing), b(range_b, slow_step, beam_distance + 2.0*plinth + 3.0*spacing), v, 0,   ptList_p[32])
Curves_C(a(range_a, slow_step, beam_distance + plinth + 2.0*spacing), b(range_b, slow_step, beam_distance + plinth + 2.0*spacing), v, 0,   ptList_p[33])
Curves_C(a(range_a, slow_step, beam_distance + plinth + spacing), b(range_b, slow_step, beam_distance + plinth + spacing), v, 0,   ptList_p[34])
Curves_C(a(range_a, slow_step, beam_distance), b(range_b, slow_step, beam_distance), v, 0,   ptList_p[35])
Curves_C(a(range_a, slow_step, 3.0 * spacing + 2.0 * plinth), b(range_b, slow_step, 3.0 * spacing + 2.0 * plinth), v, 0, ptList_p[36])
Curves_C(a(range_a, slow_step, 2.0 * spacing + plinth), b(range_b, slow_step, 2.0 * spacing + plinth), v, 0, ptList_p[37])
Curves_C(a(range_a, slow_step, spacing + plinth), b(range_b, slow_step, spacing + plinth), v, 0, ptList_p[38])
Curves_C(a(range_a, slow_step, 0), b(range_b, slow_step,0), v, 0, ptList_p[39])
'''

'''
Curves_D(0, 0, ptList_p[18])
Curves_D(plinth, ibeam_height, ptList_p[19])
Curves_D(plinth + spacing, 0, ptList_p[20])
Curves_D(plinth + spacing, ibeam_height, ptList_p[21])
Curves_D(2.0 * spacing + plinth, 0, ptList_p[22])
Curves_D(2.0 * spacing + plinth, ibeam_height, ptList_p[23])
Curves_D(3.0 * spacing + 2.0 * plinth, 0, ptList_p[24])
Curves_D(3.0 * spacing + plinth, ibeam_height, ptList_p[25])
Curves_D(beam_distance, 0,   ptList_p[26])
Curves_D(beam_distance + plinth, obeam_height,   ptList_p[27])
Curves_D(beam_distance + plinth + spacing, 0,   ptList_p[28])
Curves_D(beam_distance + plinth + spacing, obeam_height,   ptList_p[29])
Curves_D(beam_distance + plinth + 2.0*spacing, 0,   ptList_p[30])
Curves_D(beam_distance + plinth + 2.0*spacing, obeam_height,   ptList_p[31])
Curves_D(beam_distance + 2.0*plinth + 3.0*spacing, 0,   ptList_p[32])
Curves_D(beam_distance + plinth + 3.0*spacing, obeam_height,   ptList_p[33])
Curves_D(beam_distance + beam_width + br_width, plate_height,   ptList_p[34])
Curves_D(-br_width, plate_height, ptList_p[35])
'''

size = len(ptList_p[0])
new_ptList = []
n_ncurve = []

for nr_przepony in range(0, size):
    new_ptList.append(List[Point]())

for nr_przepony in range(0, size):
    for point in ptList_p:
        new_ptList[nr_przepony].Add(point[nr_przepony])

for i, ptList_point in enumerate(new_ptList):
    n_ncurve.append(NurbsCurve.CreateThroughPoints(True, ptList_point, 0.05))
    curveSegment.append(CurveSegment.Create(n_ncurve[i]))
    designCurve.append(DesignCurve.Create(GetRootPart(), curveSegment[i]))

mode = InteractionMode.Solid
result = ViewHelper.SetViewMode(mode)

Selection.Clear()
ViewHelper.ZoomToEntity()
# endblock


# Utwórz płaszczyznę odniesienia
# Record Failed
# EndBlock

# Set Sketch Plane
sectionPlane = Plane.PlaneZX
result = ViewHelper.SetSketchPlane(sectionPlane, None)
# EndBlock

# Set Sketch Plane
sectionPlane = Plane.Create(Frame.Create(Point.Create(MM(7994.99999999972), MM(-4125), MM(8500)),
                                         Direction.DirY,
                                         Direction.DirZ))
result = ViewHelper.SetSketchPlane(sectionPlane, None)
# EndBlock

# Sketch Line
start = Point2D.Create(MM(-650), MM(500))
end = Point2D.Create(MM(0), MM(0))
result = SketchLine.Create(start, end)
# EndBlock

# Sketch Line
start = Point2D.Create(MM(0), MM(0))
end = Point2D.Create(MM(200), MM(0))
result = SketchLine.Create(start, end)
# EndBlock

# Sketch Line
start = Point2D.Create(MM(200), MM(0))
end = Point2D.Create(MM(400), MM(0))
result = SketchLine.Create(start, end)
# EndBlock

# Sketch Line
start = Point2D.Create(MM(400), MM(0))
end = Point2D.Create(MM(600), MM(0))
result = SketchLine.Create(start, end)
# EndBlock

# Sketch Line
start = Point2D.Create(MM(600), MM(0))
end = Point2D.Create(MM(7650.00000018129), MM(-8.27391133384481E-06))
result = SketchLine.Create(start, end)
# EndBlock

# Sketch Line
start = Point2D.Create(MM(7650.00000018129), MM(-8.27391133384481E-06))
end = Point2D.Create(MM(7849.99999934777), MM(1.97722798134237E-05))
result = SketchLine.Create(start, end)
# EndBlock

# Sketch Line
start = Point2D.Create(MM(7849.99999934777), MM(1.97722798134237E-05))
end = Point2D.Create(MM(8049.99999992934), MM(1.63563385058296E-06))
result = SketchLine.Create(start, end)
# EndBlock

# Sketch Line
start = Point2D.Create(MM(8049.99999992934), MM(1.63563385058296E-06))
end = Point2D.Create(MM(8250.00000429254), MM(-9.03915733374561E-05))
result = SketchLine.Create(start, end)
# EndBlock

# Sketch Line
start = Point2D.Create(MM(8250.00000429254), MM(-9.03915733374561E-05))
end = Point2D.Create(MM(8899.97639655926), MM(500.038848140445))
result = SketchLine.Create(start, end)
# EndBlock

# Sketch Line
start = Point2D.Create(MM(8899.97639655926), MM(500.038848140445))
end = Point2D.Create(MM(-650), MM(500))
result = SketchLine.Create(start, end)
# EndBlock

# Solidify Sketch
mode = InteractionMode.Solid
result = ViewHelper.SetViewMode(mode, None)
# EndBlock


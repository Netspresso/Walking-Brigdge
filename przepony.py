import apex
from apex.construct import Point3D, Point2D
from apex.geometry import createPointXYZ, createCurve3DNurb
import math

apex.setScriptUnitSystem(unitSystemName=r'''mm-kg-s-N''')
applicationSettingsGeometry = apex.setting.ApplicationSettingsGeometry()
applicationSettingsGeometry.createGeometryInNewPart = apex.setting.CreateGeometryInNewPart.CurrentPart
applicationSettingsGeometry.geometryTessellationIsWatertight = False
applicationSettingsGeometry.geometryEdgeTesselationTolerance = apex.setting.GeometryTessellationTolerance.Medium
applicationSettingsGeometry.geometryFaceTesselationTolerance = apex.setting.GeometryTessellationTolerance.Medium
apex.setting.setApplicationSettingsGeometry(
    applicationSettingsGeometry=applicationSettingsGeometry)
model_1 = apex.currentModel()


class Curves:
    # Class defining curves A

    def __init__(self, a, b, Velocity, Distance, ListPoint):
        t = 0
        count = len(a)
        z = range(0, count)
        for i in z:
            self.x = a[i] * math.cos(t) - (5 * t) / (4 * math.pi) + 15
            self.y = b[i] * math.sin(t)
            self.z = Velocity * t + Distance
            ListPoint.append(
                createPointXYZ(x=self.x, y=self.y, z=self.z).asPoint())
            t += math.pi / 4.0


class Knots:
    # Class defining curves A

    def __init__(self, a, b, Velocity, Distance, ListPoint):
        t = 0
        count = len(a)
        z = range(0, count)
        for i in z:
            self.x = a[i] * math.cos(t) + 15
            self.y = b[i] * math.sin(t)
            self.z = Velocity * t + Distance
            ListPoint.append(
                createPointXYZ(x=self.x, y=self.y, z=self.z).asPoint())
            t += math.pi / 4.0


# Functions:
def a(tmax, Step, component):
    """Inner radius(f) (from center to the beam)"""
    radius = []

    t = 0
    while t <= tmax:
        radius.append((-5 / (4 * math.pi)) * t + 10 + component)
        t += Step
    return radius


def a0(tmax, Step):
    """center"""
    radius = []
    t = 0
    while t <= tmax:
        radius.append(0)
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


def linspace(low, up, leng):
    """function creating a linear space from [low] to [up] using [leng] number of elements"""
    list = []
    step = (up - low) / float(leng)
    for i in range(leng):
        list.append(low)
        low = low + step
    return list


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

n_of_curve = 21

for i in range(0, n_of_curve):
    ptList_p.append([])
# Do przeróbki:

# Do przeróbki:
Curves(a0(range_a, slow_step), a0(range_b, slow_step), v, pr_height - 0.4,
       ptList_p[0])
# //
Curves(a(range_a, slow_step, plinth), b(range_b, slow_step, plinth), v,
       ibeam_height, ptList_p[1])
Curves(a(range_a, slow_step, spacing + plinth),
       b(range_b, slow_step, spacing + plinth), v, ibeam_height, ptList_p[2])
Curves(a(range_a, slow_step, 2.0 * spacing + plinth),
       b(range_b, slow_step, 2.0 * spacing + plinth), v, ibeam_height,
       ptList_p[3])
Curves(a(range_a, slow_step, 3.0 * spacing + plinth),
       b(range_b, slow_step, 3.0 * spacing + plinth), v, ibeam_height,
       ptList_p[4])
Curves(a(range_a, slow_step, beam_distance + plinth),
       b(range_b, slow_step, beam_distance + plinth), v, obeam_height,
       ptList_p[5])
Curves(a(range_a, slow_step, beam_distance + plinth + spacing),
       b(range_b, slow_step, beam_distance + plinth + spacing), v,
       obeam_height, ptList_p[6])
Curves(a(range_a, slow_step, beam_distance + plinth + 2.0 * spacing),
       b(range_b, slow_step, beam_distance + plinth + 2.0 * spacing), v,
       obeam_height, ptList_p[7])
Curves(a(range_a, slow_step, beam_distance + plinth + 3.0 * spacing),
       b(range_b, slow_step, beam_distance + plinth + 3.0 * spacing), v,
       obeam_height, ptList_p[8])
Curves(
    a(range_a, slow_step,
      beam_distance + 2.0 * plinth + 3.0 * spacing + br_width),
    b(range_b, slow_step,
      beam_distance + 2.0 * plinth + 3.0 * spacing + br_width), v, pr_height,
    ptList_p[9])
Curves(
    a(range_a, slow_step,
      beam_distance + 2.0 * plinth + 3.0 * spacing + br_width),
    b(range_b, slow_step,
      beam_distance + 2.0 * plinth + 3.0 * spacing + br_width), v, 0,
    ptList_p[10])
Curves(a(range_a, slow_step, beam_distance + 2.0 * plinth + 3.0 * spacing),
       b(range_b, slow_step, beam_distance + 2.0 * plinth + 3.0 * spacing), v,
       0, ptList_p[11])
Curves(a(range_a, slow_step, beam_distance + plinth + 2.0 * spacing),
       b(range_b, slow_step, beam_distance + plinth + 2.0 * spacing), v, 0,
       ptList_p[12])
Curves(a(range_a, slow_step, beam_distance + plinth + spacing),
       b(range_b, slow_step, beam_distance + plinth + spacing), v, 0,
       ptList_p[13])
Curves(a(range_a, slow_step, beam_distance),
       b(range_b, slow_step, beam_distance), v, 0, ptList_p[14])
Curves(a(range_a, slow_step, 3.0 * spacing + 2.0 * plinth),
       b(range_b, slow_step, 3.0 * spacing + 2.0 * plinth), v, 0, ptList_p[15])
Curves(a(range_a, slow_step, 2.0 * spacing + plinth),
       b(range_b, slow_step, 2.0 * spacing + plinth), v, 0, ptList_p[16])
Curves(a(range_a, slow_step, spacing + plinth),
       b(range_b, slow_step, spacing + plinth), v, 0, ptList_p[17])
Curves(a(range_a, slow_step, 0), b(range_b, slow_step, 0), v, 0, ptList_p[18])
Curves(a(range_a, slow_step, -br_width), b(range_b, slow_step, -br_width), v,
       0, ptList_p[19])
Curves(a0(range_a, slow_step), a0(range_b, slow_step), v, 0, ptList_p[20])

size = len(ptList_p[10])
new_ptList = []

for nr_przepony in range(0, size):
    new_ptList.append([])
    for list in ptList_p:
        new_ptList[nr_przepony].append(list[nr_przepony])

for Curve in range(0, len(new_ptList)):
    Lista = new_ptList[Curve]
    n = len(Lista)
    deg = 1
    m = n + deg + 1
    controlPoints = Lista
    knotPoints = linspace(0, 1, m)
    createCurve3DNurb(controlPoints, knotPoints, deg).asCurve()

for i in range(21, 38):
    _target = apex.EntityCollection()
    part_1 = apex.getPart(pathName="Model/Part 1")
    curve_1 = part_1.getCurve(name="Curve {}".format(i))
    _target.extend(curve_1.getEdges())
    result = apex.geometry.fillerSurface(target=_target)